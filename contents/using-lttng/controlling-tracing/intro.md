---
id: controlling-tracing
---

Once you're in possession of a software that is properly
[instrumented](#doc-instrumenting) for LTTng tracing, be it thanks to
the built-in LTTng probes for the Linux kernel, a custom user
application or a custom Linux kernel, all that is left is actually
tracing it. As a user, you control LTTng tracing using a single command
line interface: the `lttng` tool. This tool uses `liblttng-ctl` behind
the scene to connect to and communicate with session daemons. LTTng
session daemons may either be started manually (`lttng-sessiond`) or
automatically by the `lttng` command when needed. Trace data may
be forwarded to the network and used elsewhere using an LTTng relay
daemon (`lttng-relayd`).

The man pages of `lttng`, `lttng-sessiond` and `lttng-relayd` are pretty
complete, thus this section is not an online copy of the latter (we
leave this contents for the
[Online LTTng man pages](#doc-online-lttng-manpages) section).
This section is rather a tour of LTTng
features through practical examples and tips.

If not already done, make sure you understand the core concepts
and how LTTng components connect together by reading the
[Understanding LTTng](#doc-understanding-lttng) chapter; this section
assumes you are familiar with them.
