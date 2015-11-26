---
id: installing-lttng
---

**LTTng** is a set of software components which interact to allow
instrumenting the Linux kernel and user applications as well as
controlling tracing sessions (starting/stopping tracing,
enabling/disabling events, and more). Those components are bundled into
the following packages:

  * **LTTng-tools**: libraries and command line interface to control
    tracing sessions.
  * **LTTng-modules**: Linux kernel modules for tracing the kernel.
  * **LTTng-UST**: user space tracing library.

Most distributions mark the LTTng-modules and LTTng-UST packages as
optional. In the following sections, the steps to install all three are
always provided, but note that LTTng-modules is only required if
you intend to trace the Linux kernel and LTTng-UST is only required if
you intend to trace user space applications.

This chapter shows how to install the above packages on a Linux
system. The easiest way is to use the package manager of the system's
[distribution](#doc-desktop-distributions. Embedded distributions
(Buildroot and OpenEmbedded/Yocto) currently have no packages of
LTTng 2.7 (LTTng 2.6 is available for both of them). Support is also
available for
[enterprise distributions](#doc-enterprise-distributions), such as
Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES).
Otherwise, you can
[build the LTTng packages from source](#doc-building-from-source).
