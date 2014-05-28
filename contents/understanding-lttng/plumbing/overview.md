---
id: plumbing-overview
---

As [mentioned previously](#doc-installing-lttng), the whole LTTng suite
is made of the following packages: LTTng-tools, LTTng-UST, and
LTTng-modules. Together, they provide different daemons, libraries,
kernel modules and command line interfaces. The following tree shows
which usable component belongs to which package:

  * **LTTng-tools**:
    * session daemon (`lttng-sessiond`)
    * consumer daemon (`lttng-consumerd`)
    * relay daemon (`lttng-relayd`)
    * tracing control library (`liblttng-ctl`)
    * tracing control command line tool (`lttng`)
  * **LTTng-UST**:
    * user space tracing library (`liblttng-ust`) and its headers
    * preloadable user space tracing helpers
      (`liblttng-ust-libc-wrapper`, `liblttng-ust-pthread-wrapper`,
      `liblttng-ust-cyg-profile`, `liblttng-ust-cyg-profile-fast`
      and `liblttng-ust-dl`)
    * user space tracepoint code generator command line tool
      (`lttng-gen-tp`)
    * Java Util Logging tracepoint provider (`liblttng-ust-jul-jni`)
      and JAR file (`liblttng-ust-jul.jar`)
  * **LTTng-modules**:
    * LTTng Linux kernel tracer module
    * tracing ring buffer kernel modules
    * many LTTng probe kernel modules

The following diagram shows how the most important LTTng components
interact. Plain black arrows represent trace data paths while dashed
red arrows indicate control communications. The LTTng relay daemon is
shown running on a remote system, although it could as well run on the
target (monitored) system.

<div class="img img-90">
    <object data="/images/docs/plumbing.svg" type="image/svg+xml">
        <img src="/images/docs/plumbing.svg">
    </object>
</div>

Each component is described in the following subsections.
