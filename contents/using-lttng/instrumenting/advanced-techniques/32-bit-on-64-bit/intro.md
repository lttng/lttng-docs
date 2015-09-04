---
id: instrumenting-32-bit-app-on-64-bit-system
---

In order to trace a 32-bit application running on a 64-bit system,
LTTng must use a dedicated 32-bit
[consumer daemon](#doc-lttng-consumerd). This section discusses how to
build that daemon (which is _not_ part of the default 64-bit LTTng
build) and the LTTng 32-bit tracing libraries, and how to instrument
a 32-bit application in that context.

Make sure you install all 32-bit versions of LTTng dependencies.
Their names can be found in the `README.md` files of each LTTng package
source. How to find and install them depends on your target's
Linux distribution. `gcc-multilib` is a common package name for the
multilib version of GCC, which you also need.

The following packages will be built for 32-bit support on a 64-bit
system: <a href="http://urcu.so/" class="ext">Userspace RCU</a>,
LTTng-UST and LTTng-tools.
