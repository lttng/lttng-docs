---
id: instrumenting-linux-kernel-itself
---

This section explains strictly how to add custom LTTng
instrumentation to the Linux kernel. It does not explain how the
macros actually work and the internal mechanics of the tracer.

You should have a Linux kernel source code tree to work with.
Throughout this section, all file paths are relative to the root of
this tree unless otherwise stated.

You need a copy of the LTTng-modules Git repository:

<pre class="term">
git clone git://git.lttng.org/lttng-modules.git
</pre>

The steps to add custom LTTng instrumentation to a Linux kernel
involves defining and using the mainline `TRACE_EVENT()` tracepoints
first, then writing and using the LTTng adaptation layer.
