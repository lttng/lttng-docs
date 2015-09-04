---
id: basic-tracing-session-control
---

Once you have
[created a tracing session](#doc-creating-destroying-tracing-sessions)
and [enabled one or more events](#doc-enabling-disabling-events),
you may activate the LTTng tracers for the current tracing session at
any time:

<pre class="term">
lttng start
</pre>

Subsequently, you may stop the tracers:

<pre class="term">
lttng stop
</pre>

LTTng is very flexible: user space applications may be launched before
or after the tracers are started. Events are only recorded if they
are properly enabled and if they occur while tracers are active.

A tracing session name may be passed to both the `start` and `stop`
commands to start/stop tracing a session other than the current one.
