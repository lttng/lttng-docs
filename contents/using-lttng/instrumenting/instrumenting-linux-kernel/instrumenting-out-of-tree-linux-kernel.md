---
id: instrumenting-out-of-tree-linux-kernel
---

Instrumenting a custom Linux kernel module for LTTng follows the exact
same steps as
[adding instrumentation to the Linux kernel itself](#doc-instrumenting-linux-kernel-itself),
the only difference being that your mainline tracepoint definition
header doesn't reside in the mainline source tree, but in your
kernel module source tree.

The only reference to this mainline header is in the LTTng custom
probe's source code (`probes/lttng-probe-hello.c` in our example), for
build time verification:

~~~ c
/* ... */

/* Build time verification of mismatch between mainline TRACE_EVENT()
 * arguments and LTTng adaptation layer LTTNG_TRACEPOINT_EVENT() arguments.
 */
#include <trace/events/hello.h>

/* ... */
~~~

The preferred, flexible way to include your module's mainline
tracepoint definition header is to put it in a specific directory
relative to your module's root (`tracepoints`, for example) and include it
relative to your module's root directory in the LTTng custom probe's
source:

~~~ c
#include <tracepoints/hello.h>
~~~

You may then build LTTng-modules by adding your module's root
directory as an include path to the extra C flags:

<pre class="term">
make <strong>ccflags-y=-I/path/to/kernel/module</strong> KERNELDIR=/path/to/custom/linux
</pre>

Using `ccflags-y` allows you to move your kernel module to another
directory and rebuild the LTTng-modules project with no change to
source files.
