---
id: whats-new
---

LTTng 2.7 ships with a generous list of new features, with essential
additions to all the project's components.

Dynamic filtering of user space tracepoints has been available for
quite some time now
(see [Enabling and disabling events](#doc-enabling-disabling-events)).
LTTng 2.7 adds filtering support to kernel events as well. For example:

<pre class="term">
lttng enable-event --kernel irq_handler_entry --filter 'irq == 28'
</pre>

LTTng 2.7 adds wildcard support for kernel event names:

<pre class="term">
lttng enable-event --kernel 'sched_*'
</pre>

On the user space tracing side, the new [`tracelog()`](#doc-tracelog)
facility allows users to easily migrate from logging to tracing.
`tracelog()` is similar to [`tracef()`](#doc-tracef), but accepts
an additional log level parameter.

The new `--shm-path` option of `lttng create` can be used to specify the
path where the shared memory holding the ring buffers are
created. This feature is useful when used with persistent memory file
systems to extract the latest recorded trace data in the event of a
crash requiring a reboot. The new `lttng-crash` command line
utility can extract trace data from such a file (see
[Recording trace data on persistent memory file systems](#doc-persistent-memory-file-systems)).

LTTng-UST 2.7 can rely on a user plugin to provide a custom clock source
to its tracer. LTTng-UST can also load a user plugin to retrieve the
current CPU number. This feature exists for very advanced use cases. See
the <a href="https://github.com/lttng/lttng-ust/tree/master/doc/examples/clock-override" class="ext">clock-override</a>
and <a href="https://github.com/lttng/lttng-ust/tree/master/doc/examples/getcpu-override" class="ext">getcpu-override</a>
examples for more details.

Python developers can now benefit from the new
[LTTng-UST Python agent](#doc-python-application),
a Python&nbsp;2/3-compatible package which allows standard Python logging
using the `logging` module to output log entries to an LTTng trace.

Last but not least, the new `lttng track` and `lttng untrack` commands
make [<abbr title="process ID">PID</abbr> tracking](#doc-pid-tracking)
super-fast for both the kernel and the user space domains. When one or
more PIDs are tracked, only the processes having those PIDs are allowed
to emit enabled events.

Moreover, LTTng 2.7 boasts great stability, benifiting from piles of
bug fixes and more-than-welcome internal refactorings.

<!--
To learn more about the new features of LTTng 2.7, see
<a href="" class="ext">the release announcement</a>.
-->
