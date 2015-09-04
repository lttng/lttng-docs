---
id: instrumenting
---

There are many examples of tracing and monitoring in our everyday life.
You have access to real-time and historical weather reports and forecasts
thanks to weather stations installed around the country. You know your
possibly hospitalized friends' and family's hearts are safe thanks to
electrocardiography. You make sure not to drive your car too fast
and have enough fuel to reach your destination thanks to gauges visible
on your dashboard.

All the previous examples have something in common: they rely on
**probes**. Without electrodes attached to the surface of a body's
skin, cardiac monitoring would be futile.

LTTng, as a tracer, is no different from the real life examples above.
If you're about to trace a software system, i.e. record its history of
execution, you better have probes in the subject you're
tracing: the actual software. Various ways were developed to do this.
The most straightforward one is to manually place probes, called
_tracepoints_, in the software's source code. The Linux kernel tracing
domain also allows probes added dynamically.

If you're only interested in tracing the Linux kernel, it may very well
be that your tracing needs are already appropriately covered by LTTng's
built-in Linux kernel tracepoints and other probes. Or you may be in
possession of a user space application which has already been
instrumented. In such cases, the work resides entirely in the design
and execution of tracing sessions, allowing you to jump to
[Controlling tracing](#doc-controlling-tracing) right now.

This section focuses on the following use cases of instrumentation:

  * [C](#doc-c-application) and [C++](#doc-cxx-application) applications
  * [prebuilt user space tracing helpers](#doc-prebuilt-ust-helpers)
  * [Java application](#doc-java-application)
  * [Linux kernel](#doc-instrumenting-linux-kernel) module or the
    kernel itself
  * the [`/proc/lttng-logger` <abbr title="Application Binary Interface">ABI</abbr>](#doc-proc-lttng-logger-abi)

Some [advanced techniques](#doc-advanced-instrumenting-techniques) are
also presented at the very end.
