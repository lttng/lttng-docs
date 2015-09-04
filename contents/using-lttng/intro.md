---
id: using-lttng
---

Using LTTng involves two main activities: **instrumenting** and
**controlling tracing**.

_[Instrumenting](#doc-instrumenting)_ is the process of inserting probes
into some source code. It can be done manually, by writing tracepoint
calls at specific locations in the source code of the program to trace,
or more automatically using dynamic probes (address in assembled code,
symbol name, function entry/return, and others).

It has to be noted that, as an LTTng user, you may not have to worry
about the instrumentation process. Indeed, you may want to trace a
program already instrumented. As an example, the Linux kernel is
thoroughly instrumented, which is why you can trace it without caring
about adding probes.

_[Controlling tracing](#doc-controlling-tracing)_ is everything
that can be done by the LTTng session daemon, which is controlled using
`liblttng-ctl` or its command line utility, `lttng`: creating tracing
sessions, listing tracing sessions and events, enabling/disabling
events, starting/stopping the tracers, taking snapshots, amongst many
other commands.

This chapter is a complete user guide of both activities,
with common use cases of LTTng exposed throughout the text. It is
assumed that you are familiar with LTTng's concepts (events, channels,
domains, tracing sessions) and that you understand the roles of its
components (daemons, libraries, command line tools); if not, we invite
you to read the [Understanding LTTng](#doc-understanding-lttng) chapter
before you begin reading this one.

If you're new to LTTng, we suggest that you rather start with the
[Getting started](#doc-getting-started) small guide first, then come
back here to broaden your knowledge.

If you're only interested in tracing the Linux kernel with its current
instrumentation, you may skip the
[Instrumenting](#doc-instrumenting) section.
