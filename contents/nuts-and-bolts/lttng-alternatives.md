---
id: lttng-alternatives
---

Excluding proprietary solutions, a few competing software tracers
exist for Linux:

  * <a href="https://www.kernel.org/doc/Documentation/trace/ftrace.txt" class="ext">ftrace</a>
    is the de facto function tracer of the Linux kernel. Its user
    interface is a set of special files in sysfs.
  * <a href="https://perf.wiki.kernel.org/" class="ext">perf</a> is
    a performance analyzing tool for Linux which supports hardware
    performance counters, tracepoints, as well as other counters and
    types of probes. perf's controlling utility is the `perf` command
    line/curses tool.
  * <a href="http://linux.die.net/man/1/strace" class="ext">strace</a>
    is a command line utility which records system calls made by a
    user process, as well as signal deliveries and changes of process
    state. strace makes use of
    <a href="https://en.wikipedia.org/wiki/Ptrace" class="ext">ptrace</a>
    to fulfill its function.
  * <a href="https://sourceware.org/systemtap/" class="ext">SystemTap</a>
    is a Linux kernel and user space tracer which uses custom user scripts
    to produce plain text traces. Scripts are converted to the C language,
    then compiled as Linux kernel modules which are loaded to produce
    trace data. SystemTap's primary user interface is the `stap`
    command line tool.
  * <a href="http://www.sysdig.org/" class="ext">sysdig</a>, like
    SystemTap, uses scripts to analyze Linux kernel events. Scripts,
    or _chisels_ in sysdig's jargon, are written in Lua and executed
    while the system is being traced, or afterwards. sysdig's interface
    is the `sysdig` command line tool as well as the curses-based
    `csysdig` tool.

The main distinctive features of LTTng is that it produces correlated
kernel and user space traces, as well as doing so with the lowest
overhead amongst other solutions. It produces trace files in the
<a href="http://diamon.org/ctf" class="ext"><abbr title="Common Trace Format">CTF</abbr></a>
format, an optimized file format for production and analyses of
multi-gigabyte data. LTTng is the result of close to 10 years of
active development by a community of passionate developers. It is
currently available on all major desktop, server, and embedded Linux
distributions.

The main interface for tracing control is a single command line tool
named `lttng`. The latter can create several tracing sessions,
enable/disable events on the fly, filter them efficiently with custom
user expressions, start/stop tracing, and do much more. Traces can be
recorded on disk or sent over the network, kept totally or partially,
and viewed once tracing becomes inactive or in real-time.

[Install LTTng now](#doc-installing-lttng) and start tracing!
