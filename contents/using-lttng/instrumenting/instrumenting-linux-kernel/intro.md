---
id: instrumenting-linux-kernel
---

The Linux kernel can be instrumented for LTTng tracing, either its core
source code or a kernel module. It has to be noted that Linux is
readily traceable using LTTng since many parts of its source code are
already instrumented: this is the job of the upstream
<a href="http://git.lttng.org/?p=lttng-modules.git" class="ext">LTTng-modules</a>
package. This section presents how to add LTTng instrumentation where it
does not currently exist and how to instrument custom kernel modules.

All LTTng instrumentation in the Linux kernel is based on an existing
infrastructure which bears the name of its main macro, `TRACE_EVENT()`.
This macro is used to define tracepoints,
each tracepoint having a name, usually with the
<code><em>subsys</em>_<em>name</em></code> format,
<code><em>subsys</em></code> being the subsystem name and
<code><em>name</em></code> the specific event name.

Tracepoints defined with `TRACE_EVENT()` may be inserted anywhere in
the Linux kernel source code, after what callbacks, called _probes_,
may be registered to execute some action when a tracepoint is
executed. This mechanism is directly used by ftrace and perf,
but cannot be used as is by LTTng: an adaptation layer is added to
satisfy LTTng's specific needs.

With that in mind, this documentation does not cover the `TRACE_EVENT()`
format and how to use it, but it is mandatory to understand it and use
it to instrument Linux for LTTng. A series of
<abbr title="Linux Weekly News">LWN</abbr> articles explain
`TRACE_EVENT()` in details:
<a href="http://lwn.net/Articles/379903/" class="ext">part 1</a>,
<a href="http://lwn.net/Articles/381064/" class="ext">part 2</a>, and
<a href="http://lwn.net/Articles/383362/" class="ext">part 3</a>.
Once you master `TRACE_EVENT()` enough for your use case, continue
reading this section so that you can add the LTTng adaptation layer of
instrumentation.

This section first discusses the general method of instrumenting the
Linux kernel for LTTng. This method is then reused for the specific
case of instrumenting a kernel module.
