---
id: nuts-and-bolts
---

What is LTTng? As its name suggests, the
_Linux Trace Toolkit: next generation_ is a modern toolkit for
tracing Linux systems and applications. So your first question might
rather be: **what is tracing?**

As the history of software engineering progressed and led to what
we now take for granted&mdash;complex, numerous and
interdependent software applications running in parallel on
sophisticated operating systems like Linux&mdash;the authors of such
components, or software developers, began feeling a natural
urge of having tools to ensure the robustness and good performance
of their masterpieces.

One major achievement in this field is, inarguably, the
<a href="https://www.gnu.org/software/gdb/" class="ext">GNU debugger
(GDB)</a>, which is an essential tool for developers to find and fix
bugs. But even the best debugger won't help make your software run
faster, and nowadays, faster software means either more work done by
the same hardware, or cheaper hardware for the same work.

A _profiler_ is often the tool of choice to identify performance
bottlenecks. Profiling is suitable to identify _where_ performance is
lost in a given software; the profiler outputs a profile, a
statistical summary of observed events, which you may use to know
which functions took the most time to execute. However, a profiler
won't report _why_ some identified functions are the bottleneck.
Also, bottlenecks might only occur when specific conditions are met.
For a thorough investigation of software performance issues, a history
of execution, with historical values of chosen variables, is
essential. This is where tracing comes in handy.

_Tracing_ is a technique used to understand what goes on in a running
software system. The software used for tracing is called a _tracer_,
which is conceptually similar to a tape recorder. When recording,
specific points placed in the software source code generate events
that are saved on a giant tape: a _trace_ file. Both user applications
and the operating system may be traced at the same time, opening the
possibility of resolving a wide range of problems that are otherwise
extremely challenging.

Tracing is often compared to _logging_. However, tracers and loggers
are two different types of tools, serving two different purposes. Tracers are
designed to record much lower-level events that occur much more
frequently than log messages, often in the thousands per second range,
with very little execution overhead. Logging is more appropriate for
very high-level analysis of less frequent events: user accesses,
exceptional conditions (errors and warnings, for example), database
transactions, instant messaging communications, etc. More formally,
logging is one of several use cases that can be accomplished with
tracing.

The list of recorded events inside a trace file may be read manually
like a log file for the maximum level of detail, but it is generally
much more interesting to perform application-specific analyses to
produce reduced statistics and graphs that are useful to resolve a
given problem. Trace viewers and analysers are specialized tools which
achieve this.

So, in the end, this is what LTTng is: a powerful, open source set of
tools to trace the Linux kernel and user applications. LTTng is
composed of several components actively maintained and developed by
its <a href="/community/#where" class="ext">community</a>.

Excluding proprietary solutions, a few competing software tracers
exist for Linux.
<a href="https://www.kernel.org/doc/Documentation/trace/ftrace.txt" class="ext">ftrace</a>
is the de facto function tracer of the Linux kernel.
<a href="http://linux.die.net/man/1/strace" class="ext">strace</a>
is able to record all system calls made by a user process.
<a href="https://sourceware.org/systemtap/" class="ext">SystemTap</a>
is a Linux kernel and user space tracer which uses custom user scripts
to produce plain text traces.
<a href="http://www.sysdig.org/" class="ext">sysdig</a>
also uses scripts, written in Lua, to trace and analyze the Linux
kernel.

The main distinctive features of LTTng is that it produces correlated
kernel and user space traces, as well as doing so with the lowest
overhead amongst other solutions.  It produces trace files in the
<a href="http://www.efficios.com/ctf" class="ext"><abbr title="Common Trace Format">CTF</abbr></a>
format, an optimized file format for production and analyses of
multi-gigabyte data. LTTng is the result of close to 10 years of
active development by a community of passionate developers. It is
currently available on all major desktop, server, and embedded Linux
distributions.

The main interface for tracing control is a single command line tool
named `lttng`. The latter can create several tracing sessions,
enable/disable events on the fly, filter them efficiently with custom
user expressions, start/stop tracing and do much more. Traces can be
recorded on disk or sent over the network, kept totally or partially,
and viewed once tracing is inactive or in real-time.

[Install LTTng now](#doc-installing-lttng) and start tracing!
