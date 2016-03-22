---
id: lttng-tracepoint-event-code
since: 2.7
---

Although it is recommended to always use the
[`LTTNG_TRACEPOINT_EVENT()`](#doc-lttng-adaptation-layer)
macro to describe the arguments and fields of an LTTng tracepoint when
possible, sometimes a more complex process is needed to access the data
to be recorded as tracepoint fields. In other words, local variables
and multiple C statements are required instead of simple argument-based
expressions passed to the
[`ctf_*()` macros of `TP_FIELDS()`](#doc-lttng-modules-tp-fields).

The `LTTNG_TRACEPOINT_EVENT_CODE()` macro can be used instead of
`LTTNG_TRACEPOINT_EVENT()` to declare custom local variables and
define a block of C code to be executed before the fields are
recorded. The structure of this macro is:

~~~ c
LTTNG_TRACEPOINT_EVENT_CODE(
    /* format identical to LTTNG_TRACEPOINT_EVENT() version for those */
    hello_world,
    TP_PROTO(int foo, const char *bar),
    TP_ARGS(foo, bar),

    /* declarations of custom local variables */
    TP_locvar(
        int a = 0;
        unsigned long b = 0;
        const char *name = "(undefined)";
        struct my_struct *my_struct;
    ),

    /*
     * Custom code using which use both tracepoint arguments
     * (in TP_ARGS()) and local variables (in TP_locvar()).
     *
     * Local variables are actually members of a structure pointed
     * to by the special variable tp_locvar.
     */
    TP_code(
        if (foo) {
            tp_locvar->a = foo + 17;
            tp_locvar->my_struct = get_my_struct_at(tp_locvar->a);
            tp_locvar->b = my_struct_compute_b(tp_locvar->my_struct);
            tp_locvar->name = my_struct_get_name(tp_locvar->my_struct);
            put_my_struct(tp_locvar->my_struct);

            if (tp_locvar->b) {
                tp_locvar->a = 1;
            }
        }
    ),

    /*
     * Format identical to LTTNG_TRACEPOINT_EVENT() version for this,
     * except that tp_locvar members can be used in the argument
     * expression parameters of the ctf_*() macros.
     */
    TP_FIELDS(
        ctf_integer(unsigned long, my_struct_b, tp_locvar->b)
        ctf_integer(int, my_struct_a, tp_locvar->a)
        ctf_string(bar_field, bar)
        ctf_string(my_struct_name, tp_locvar->name)
    )
)
~~~

Make sure that the C code defined in `TP_code()` has no side effects
when executed. In particular, the code should not allocate memory or get
resources without deallocating this memory or putting those resources
afterwards.
