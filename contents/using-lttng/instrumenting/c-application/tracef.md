---
id: tracef
since: 2.5
---

`tracef()` is a small LTTng-UST API to avoid defining your own
tracepoints and tracepoint providers. The signature of `tracef()` is
the same as `printf()`'s.

The `tracef()` utility function was developed to make user space tracing
super simple, albeit with notable disadvantages compared to custom,
full-fledged tracepoint providers:

  * All generated events have the same provider/event names, respectively
    `lttng_ust_tracef` and `event`.
  * There's no static type checking.
  * The only event field you actually get, named `msg`, is a string
    potentially containing the values you passed to the function
    using your own format. This also means that you cannot use filtering
    using a custom expression at runtime because there are no isolated
    fields.
  * Since `tracef()` uses C standard library's `vasprintf()` function
    in the background to format the strings at runtime, its
    expected performance is lower than using custom tracepoint providers
    with typed fields, which do not require a conversion to a string.

Thus, `tracef()` is useful for quick prototyping and debugging, but
should not be considered for any permanent/serious application
instrumentation.

To use `tracef()`, first include `<lttng/tracef.h>` in the C source file
where you need to insert probes:

~~~ c
#include <lttng/tracef.h>
~~~

Use `tracef()` like you would use `printf()` in your source code, for
example:

~~~ c
    /* ... */

    tracef("my message, my integer: %d", my_integer);

    /* ... */
~~~

Link your application with `liblttng-ust`:

<pre class="term">
gcc -o app app.c <strong>-llttng-ust</strong>
</pre>

Execute the application as usual:

<pre class="term">
./app
</pre>

Voilà! Use the `lttng` command line tool to
[control tracing](#doc-controlling-tracing). You can enable `tracef()`
events like this:

<pre class="term">
lttng enable-event --userspace 'lttng_ust_tracef:*'
</pre>
