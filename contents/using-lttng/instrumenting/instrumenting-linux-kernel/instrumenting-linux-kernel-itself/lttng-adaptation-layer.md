---
id: lttng-adaptation-layer
---

The steps to write the LTTng adaptation layer are, in your
LTTng-modules copy's source code tree:

  1. In `instrumentation/events/lttng-module`,
     add a header <code><em>subsys</em>.h</code> for your custom
     subsystem <code><em>subsys</em></code> and write your
     tracepoint definitions using LTTng-modules macros in it.
     Those macros look like the mainline kernel equivalents,
     but they present subtle, yet important differences.
  2. In `probes`, create the C source file of the LTTng probe kernel
     module for your subsystem. It should be named
     <code>lttng-probe-<em>subsys</em>.c</code>.
  3. Edit `probes/Makefile` so that the LTTng-modules project
     builds your custom LTTng probe kernel module.
  4. Build and install LTTng kernel modules.

Following our `hello_world` event example, here's the content of
`instrumentation/events/lttng-module/hello.h`:

~~~ c
#undef TRACE_SYSTEM
#define TRACE_SYSTEM hello

#if !defined(_TRACE_HELLO_H) || defined(TRACE_HEADER_MULTI_READ)
#define _TRACE_HELLO_H

#include "../../../probes/lttng-tracepoint-event.h"
#include <linux/tracepoint.h>

LTTNG_TRACEPOINT_EVENT(
    /* format identical to mainline version for those */
    hello_world,
    TP_PROTO(int foo, const char* bar),
    TP_ARGS(foo, bar),

    /* possible differences */
    TP_STRUCT__entry(
        __field(int, my_int)
        __field(char, char0)
        __field(char, char1)
        __string(product, bar)
    ),

    /* notice the use of tp_assign()/tp_strcpy() and no semicolons */
    TP_fast_assign(
        tp_assign(my_int, foo)
        tp_assign(char0, bar[0])
        tp_assign(char1, bar[1])
        tp_strcpy(product, bar)
    ),

    /* This one is actually not used by LTTng either, but must be
     * present for the moment.
     */
    TP_printk("", 0)

/* no semicolon after this either */
)

#endif

/* other difference: do NOT include <trace/define_trace.h> */
#include "../../../probes/define_trace.h"
~~~

Some possible entries for `TP_STRUCT__entry()` and `TP_fast_assign()`,
in the case of LTTng-modules, are shown in the
[LTTng-modules reference](#doc-lttng-modules-ref) section.

The best way to learn how to use the above macros is to inspect
existing LTTng tracepoint definitions in `instrumentation/events/lttng-module`
header files. Compare them with the Linux kernel mainline versions
in `include/trace/events`.

The next step is writing the LTTng probe kernel module C source file.
This one is named <code>lttng-probe-<em>subsys</em>.c</code>
in `probes`. You may always use the following template:

~~~ c
#include <linux/module.h>
#include "../lttng-tracer.h"

/* Build time verification of mismatch between mainline TRACE_EVENT()
 * arguments and LTTng adaptation layer LTTNG_TRACEPOINT_EVENT() arguments.
 */
#include <trace/events/hello.h>

/* create LTTng tracepoint probes */
#define LTTNG_PACKAGE_BUILD
#define CREATE_TRACE_POINTS
#define TRACE_INCLUDE_PATH ../instrumentation/events/lttng-module

#include "../instrumentation/events/lttng-module/hello.h"

MODULE_LICENSE("GPL and additional rights");
MODULE_AUTHOR("Your name <your-email>");
MODULE_DESCRIPTION("LTTng hello probes");
MODULE_VERSION(__stringify(LTTNG_MODULES_MAJOR_VERSION) "."
    __stringify(LTTNG_MODULES_MINOR_VERSION) "."
    __stringify(LTTNG_MODULES_PATCHLEVEL_VERSION)
    LTTNG_MODULES_EXTRAVERSION);
~~~

Just replace `hello` with your subsystem name. In this example,
`<trace/events/hello.h>`, which is the original mainline tracepoint
definition header, is included for verification purposes: the
LTTng-modules build system is able to emit an error at build time when
the arguments of the mainline `TRACE_EVENT()` definitions do not match
the ones of the LTTng-modules adaptation layer
(`LTTNG_TRACEPOINT_EVENT()`).

Edit `probes/Makefile` and add your new kernel module object
next to existing ones:

~~~ makefile
# ...

obj-m += lttng-probe-module.o
obj-m += lttng-probe-power.o

obj-m += lttng-probe-hello.o

# ...
~~~

Time to build! Point to your custom Linux kernel source tree using
the `KERNELDIR` variable:

<pre class="term">
make <strong>KERNELDIR=/path/to/custom/linux</strong>
</pre>

Finally, install modules:

<pre class="term">
sudo make modules_install
</pre>
