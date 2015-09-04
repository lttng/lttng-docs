---
id: tracelog
since: 2.7
---

The `tracelog()` API is very similar to [`tracef()`](#doc-tracef). The
only difference is that it accepts an additional log level parameter.

The goal of `tracelog()` is to ease the migration from logging to
tracing.

Here's an example:

~~~ c
#include <lttng/tracelog.h>

void my_function(int my_integer) {
    /* ... */

    tracelog(TRACE_INFO, "my message, my integer: %d", my_integer);

    /* ... */
}
~~~

See [LTTng-UST library reference](#doc-liblttng-ust-tracepoint-loglevel)
for the list of available log level names.

Link your application with `liblttng-ust`:

<pre class="term">
gcc -o app app.c <strong>-llttng-ust</strong>
</pre>

Execute the application as usual:

<pre class="term">
./app
</pre>

The events produced by `tracelog()` calls are prefixed with
`lttng_ust_tracelog:`. To enable `tracelog()` events matching a range
of log levels, do:

<pre class="term">
lttng enable-event --userspace 'lttng_ust_tracelog:*' \
                   --loglevel TRACE_INFO
</pre>

This enables all `tracelog()` events with a log level at least as important
as `TRACE_INFO`.

To enable `tracelog()` events matching a specific log level, do:

<pre class="term">
lttng enable-event --userspace 'lttng_ust_tracelog:*' \
                   --loglevel-only TRACE_WARNING
</pre>

See [Enabling and disabling events](#doc-enabling-disabling-events) for
more options.
