---
id: what-is-tracing
---

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
statistical summary of observed events, which you may use to discover
which functions took the most time to execute. However, a profiler
won't report _why_ some identified functions are the bottleneck.
Bottlenecks might only occur when specific conditions are met, sometimes
almost impossible to capture by a statistical profiler, or impossible to
reproduce with an application altered by the overhead of an event-based
profiler. For a thorough investigation of software performance issues,
a history of execution, with the recorded values of chosen variables
and context, is essential. This is where tracing comes in handy.

_Tracing_ is a technique used to understand what goes on in a running
software system. The software used for tracing is called a _tracer_,
which is conceptually similar to a tape recorder. When recording,
specific probes placed in the software source code generate events
that are saved on a giant tape: a _trace_ file. Both user applications
and the operating system may be traced at the same time, opening the
possibility of resolving a wide range of problems that are otherwise
extremely challenging.

Tracing is often compared to _logging_. However, tracers and loggers
are two different tools, serving two different purposes. Tracers are
designed to record much lower-level events that occur much more
frequently than log messages, often in the thousands per second range,
with very little execution overhead. Logging is more appropriate for
very high-level analysis of less frequent events: user accesses,
exceptional conditions (errors and warnings, for example), database
transactions, instant messaging communications, and such. More formally,
logging is one of several use cases that can be accomplished with
tracing.

The list of recorded events inside a trace file may be read manually
like a log file for the maximum level of detail, but it is generally
much more interesting to perform application-specific analyses to
produce reduced statistics and graphs that are useful to resolve a
given problem. Trace viewers and analysers are specialized tools
designed to do this.

So, in the end, this is what LTTng is: a powerful, open source set of
tools to trace the Linux kernel and user applications at the same time.
LTTng is composed of several components actively maintained and
developed by its <a href="/community/#where" class="ext">community</a>.
