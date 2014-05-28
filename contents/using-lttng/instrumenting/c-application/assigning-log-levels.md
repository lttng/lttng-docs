---
id: assigning-log-levels
---

Optionally, a log level can be assigned to a defined tracepoint.
Assigning different levels of importance to tracepoints can be useful;
when controlling tracing sessions,
[you can choose](#doc-controlling-tracing) to only enable tracepoints
falling into a specific log level range.

Log levels are assigned to defined tracepoints using the
`TRACEPOINT_LOGLEVEL()` macro. The latter must be used _after_ having
used `TRACEPOINT_EVENT()` for a given tracepoint. The
`TRACEPOINT_LOGLEVEL()` macro has the following construct:

~~~ c
TRACEPOINT_LOGLEVEL(<provider name>, <tracepoint name>, <log level>)
~~~

where the first two arguments are the same as the first two arguments
of `TRACEPOINT_EVENT()` and `<log level>` is one
of the values given in the
[LTTng-UST library reference](#doc-liblttng-ust-tracepoint-loglevel)
section.

As an example, let's assign a `TRACE_DEBUG_UNIT` log level to our
previous tracepoint definition:

~~~ c
TRACEPOINT_LOGLEVEL(my_provider, my_tracepoint, TRACE_DEBUG_UNIT)
~~~
