---
id: using-tracepoint-classes
---

In LTTng-UST, a _tracepoint class_ is a class of tracepoints sharing the
same field types and names. A _tracepoint instance_ is one instance of
such a declared tracepoint class, with its own event name and tracepoint
provider name.

What is documented in [Defining tracepoints](#doc-defining-tracepoints)
is actually how to declare a _tracepoint class_ and define a
_tracepoint instance_ at the same time. Without revealing the internals
of LTTng-UST too much, it has to be noted that one serialization
function is created for each tracepoint class. A serialization
function is responsible for serializing the fields of a tracepoint
into a sub-buffer when tracing. For various performance reasons, when
your situation requires multiple tracepoints with different names, but
with the same fields layout, the best practice is to manually create
a tracepoint class and instantiate as many tracepoint instances as
needed. One positive effect of such a design, amongst other advantages,
is that all tracepoint instances of the same tracepoint class
reuse the same serialization function, thus reducing cache pollution.

As an example, here are three tracepoint definitions as we know them:

~~~ c
TRACEPOINT_EVENT(
    my_app,
    get_account,
    TP_ARGS(
        int, userid,
        size_t, len
    ),
    TP_FIELDS(
        ctf_integer(int, userid, userid)
        ctf_integer(size_t, len, len)
    )
)

TRACEPOINT_EVENT(
    my_app,
    get_settings,
    TP_ARGS(
        int, userid,
        size_t, len
    ),
    TP_FIELDS(
        ctf_integer(int, userid, userid)
        ctf_integer(size_t, len, len)
    )
)

TRACEPOINT_EVENT(
    my_app,
    get_transaction,
    TP_ARGS(
        int, userid,
        size_t, len
    ),
    TP_FIELDS(
        ctf_integer(int, userid, userid)
        ctf_integer(size_t, len, len)
    )
)
~~~

In this case, three tracepoint classes are created, with one tracepoint
instance for each of them: `get_account`, `get_settings` and
`get_transaction`. However, they all share the same field names and
types. Declaring one tracepoint class and three tracepoint instances of
the latter is a better design choice:

~~~ c
/* the tracepoint class */
TRACEPOINT_EVENT_CLASS(
    /* tracepoint provider name */
    my_app,

    /* tracepoint class name */
    my_class,

    /* arguments */
    TP_ARGS(
        int, userid,
        size_t, len
    ),

    /* fields */
    TP_FIELDS(
        ctf_integer(int, userid, userid)
        ctf_integer(size_t, len, len)
    )
)

/* the tracepoint instances */
TRACEPOINT_EVENT_INSTANCE(
    /* tracepoint provider name */
    my_app,

    /* tracepoint class name */
    my_class,

    /* tracepoint/event name */
    get_account,

    /* arguments */
    TP_ARGS(
        int, userid,
        size_t, len
    )
)
TRACEPOINT_EVENT_INSTANCE(
    my_app,
    my_class,
    get_settings,
    TP_ARGS(
        int, userid,
        size_t, len
    )
)
TRACEPOINT_EVENT_INSTANCE(
    my_app,
    my_class,
    get_transaction,
    TP_ARGS(
        int, userid,
        size_t, len
    )
)
~~~

Of course, all those names and `TP_ARGS()` invocations are redundant,
but some C preprocessor magic can solve this:

~~~ c
#define MY_TRACEPOINT_ARGS \
    TP_ARGS( \
        int, userid, \
        size_t, len \
    )

TRACEPOINT_EVENT_CLASS(
    my_app,
    my_class,
    MY_TRACEPOINT_ARGS,
    TP_FIELDS(
        ctf_integer(int, userid, userid)
        ctf_integer(size_t, len, len)
    )
)

#define MY_APP_TRACEPOINT_INSTANCE(name) \
    TRACEPOINT_EVENT_INSTANCE( \
        my_app, \
        my_class, \
        name, \
        MY_TRACEPOINT_ARGS \
    )

MY_APP_TRACEPOINT_INSTANCE(get_account)
MY_APP_TRACEPOINT_INSTANCE(get_settings)
MY_APP_TRACEPOINT_INSTANCE(get_transaction)
~~~
