---
id: buildroot
---

LTTng packages in Buildroot are `lttng-tools`, `lttng-modules` and
`lttng-libust`.

To enable them, start the Buildroot configuration menu as usual:

<pre class="term">
make menuconfig
</pre>

In:

  * _Kernel_: make sure _Linux kernel_ is enabled
  * _Toolchain_: make sure the following options are enabled:
    * _Enable large file (files > 2GB) support_
    * _Enable WCHAR support_

In _Target packages_/_Debugging, profiling and benchmark_, enable
_lttng-modules_ and _lttng-tools_. In
_Target packages_/_Libraries_/_Other_, enable _lttng-libust_.
