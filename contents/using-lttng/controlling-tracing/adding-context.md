---
id: adding-context
---

If you read all the sections of
[Controlling tracing](#doc-controlling-tracing) so far, you should be
able to create tracing sessions, create and enable channels and events
within them and start/stop the LTTng tracers. Event fields recorded in
trace files provide important information about occurring events, but
sometimes external context may help you solve a problem faster. This
section discusses how to add context information to events of a
specific channel using the `lttng` tool.

There are various available context values which can accompany events
recorded by LTTng, for example:

  * **process information**:
    * identifier (PID)
    * name
    * priority
    * scheduling priority (niceness)
    * thread identifier (TID)
  * the **hostname** of the system on which the event occurred
  * plenty of **performance counters** using perf, for example:
    * CPU cycles, stalled cycles, idle cycles, and the other cycle types
    * cache misses
    * branch instructions, misses, loads
    * CPU faults

The full list is available in the output of `lttng add-context --help`.
Some of them are reserved for a specific domain (kernel or
user space) while others are available for both.

To add context information to one or all channels of a given tracing
session, use the `add-context` command:

<pre class="term">
lttng add-context --userspace --type vpid --type perf:thread:cpu-cycles
</pre>

The above example adds the virtual process identifier and per-thread
CPU cycles count values to all recorded user space domain events of the
current tracing session. Use the `--channel` option to select a specific
channel:

<pre class="term">
lttng add-context --kernel --channel my-channel --type tid
</pre>

adds the thread identifier value to all recorded kernel domain events
in the channel `my-channel` of the current tracing session.

Beware that context information cannot be removed from channels once
it's added for a given tracing session.
