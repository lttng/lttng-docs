---
id: installing-lttng
---

**LTTng** is a set of software components which interact to allow
instrumenting the Linux kernel and user applications and controlling
tracing sessions (starting/stopping tracing, enabling/disabling events,
etc.). Those components are bundled into the following packages:

  * **LTTng-tools**: Libraries and command line interface to control
    tracing sessions
  * **LTTng-modules**: Linux kernel modules allowing Linux to be
    traced using LTTng
  * **LTTng-UST**: User space tracing library

Most distributions mark the LTTng-modules and LTTng-UST packages as
optional. In the following sections, we always provide the steps to
install all three, but be aware that LTTng-modules is only required if
you intend to trace the Linux kernel and LTTng-UST is only required if
you intend to trace user space applications.

This chapter shows how to install the above packages on a Linux
system. The easiest way is to use the package manager of the system's
distribution ([desktop](#doc-desktop-distributions) or
[embedded](#doc-embedded-distributions)). Otherwise, you can
[build the LTTng packages from source](#doc-building-from-source).
