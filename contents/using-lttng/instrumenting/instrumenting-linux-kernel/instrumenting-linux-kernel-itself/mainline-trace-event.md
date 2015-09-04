---
id: mainline-trace-event
---

The first step is to define tracepoints using the mainline Linux
`TRACE_EVENT()` macro and insert tracepoints where you want them.
Your tracepoint definitions reside in a header file in
`include/trace/events`. If you're adding tracepoints to an existing
subsystem, edit its appropriate header file.

As an example, the following header file (let's call it
`include/trace/events/hello.h`) defines one tracepoint using
`TRACE_EVENT()`:

~~~ c
/* subsystem name is "hello" */
#undef TRACE_SYSTEM
#define TRACE_SYSTEM hello

#if !defined(_TRACE_HELLO_H) || defined(TRACE_HEADER_MULTI_READ)
#define _TRACE_HELLO_H

#include <linux/tracepoint.h>

TRACE_EVENT(
    /* "hello" is the subsystem name, "world" is the event name */
    hello_world,

    /* tracepoint function prototype */
    TP_PROTO(int foo, const char* bar),

    /* arguments for this tracepoint */
    TP_ARGS(foo, bar),

    /* LTTng doesn't need those */
    TP_STRUCT__entry(),
    TP_fast_assign(),
    TP_printk("", 0)
);

#endif

/* this part must be outside protection */
#include <trace/define_trace.h>
~~~

Notice that we don't use any of the last three arguments: they
are left empty here because LTTng doesn't need them. You would only fill
`TP_STRUCT__entry()`, `TP_fast_assign()` and `TP_printk()` if you were
to also use this tracepoint for ftrace/perf.

Once this is done, you may place calls to `trace_hello_world()`
wherever you want in the Linux source code. As an example, let us place
such a tracepoint in the `usb_probe_device()` static function
(`drivers/usb/core/driver.c`):

~~~ c
/* called from driver core with dev locked */
static int usb_probe_device(struct device *dev)
{
    struct usb_device_driver *udriver = to_usb_device_driver(dev->driver);
    struct usb_device *udev = to_usb_device(dev);
    int error = 0;

    trace_hello_world(udev->devnum, udev->product);

    /* ... */
}
~~~

This tracepoint should fire every time a USB device is plugged in.

At the top of `driver.c`, we need to include our actual tracepoint
definition and, in this case (one place per subsystem), define
`CREATE_TRACE_POINTS`, which creates our tracepoint:

~~~ c
/* ... */

#include "usb.h"

#define CREATE_TRACE_POINTS
#include <trace/events/hello.h>

/* ... */
~~~

Build your custom Linux kernel. In order to use LTTng, make sure the
following kernel configuration options are enabled:

  * `CONFIG_MODULES` (loadable module support)
  * `CONFIG_KALLSYMS` (load all symbols for debugging/kksymoops)
  * `CONFIG_HIGH_RES_TIMERS` (high resolution timer support)
  * `CONFIG_TRACEPOINTS` (kernel tracepoint instrumentation)

Boot the custom kernel. The directory
`/sys/kernel/debug/tracing/events/hello` should exist if everything
went right, with a `hello_world` subdirectory.
