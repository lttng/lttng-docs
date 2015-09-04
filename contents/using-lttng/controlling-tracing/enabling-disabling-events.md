---
id: enabling-disabling-events
---

Inside a tracing session, individual events may be enabled or disabled
so that tracing them may or may not generate trace data.

We sometimes use the term _event_ metonymically throughout this text to
refer to a specific condition, or _rule_, that could lead, when
satisfied, to an actual occurring event (a point at a specific position
in source code/binary program, logical processor and time capturing
some payload) being recorded as trace data. This specific condition is
composed of:

  1. A **domain** (kernel, user space, `java.util.logging`, or log4j)
     (required).
  2. One or many **instrumentation points** in source code or binary
     program (tracepoint name, address, symbol name, function name,
     logger name, amongst other types of probes) to be executed (required).
  3. A **log level** (each instrumentation point declares its own log
     level) or log level range to match (optional; only valid for user
     space domain).
  4. A **custom user expression**, or **filter**, that must evaluate to
     _true_ when a tracepoint is executed (optional; only valid for user
     space domain).

All conditions are specified using arguments passed to the
`enable-event` command of the `lttng` tool.

Condition 1 is specified using either `--kernel`/`-k` (kernel),
`--userspace`/`-u` (user space), `--jul`/`-j`
(<abbr title="java.util.logging">JUL</abbr>), or `--log4j`/`-l` (log4j).
Exactly one of those four arguments must be specified.

Condition 2 is specified using one of:

  * `--tracepoint`: **tracepoint**
  * `--probe`: **dynamic probe** (address, symbol name  or combination
    of both in binary program; only valid for kernel domain)
  * `--function`: **function entry/exit** (address, symbol name or
    combination of both in binary program; only valid for kernel domain)
  * `--syscall`: **system call entry/exit** (only valid for kernel
    domain)

When none of the above is specified, `enable-event` defaults to
using `--tracepoint`.

Condition 3 is specified using one of:

  * `--loglevel`: log level range from 0 to a specific log level
  * `--loglevel-only`: specific log level

See `lttng enable-event --help` for the complete list of log level
names.

Condition 4 is specified using the `--filter` option. This filter is
a C-like expression, potentially reading real-time values of event
fields, that has to evaluate to _true_ for the condition to be satisfied.
Event fields are read using plain identifiers while context fields
must be prefixed with `$ctx.`. See `lttng enable-event --help` for
all usage details.

The aforementioned arguments are combined to create and enable events.
Each unique combination of arguments leads to a different
_enabled event_. The log level and filter arguments are optional, their
default values being respectively all log levels and a filter which
always returns _true_.

Here are a few examples (you must
[create a tracing session](#doc-creating-destroying-tracing-sessions)
first):

<pre class="term">
lttng enable-event -u --tracepoint my_app:hello_world
lttng enable-event -u --tracepoint my_app:hello_you --loglevel TRACE_WARNING
lttng enable-event -u --tracepoint 'my_other_app:*'
lttng enable-event -u --tracepoint my_app:foo_bar \
                   --filter 'some_field <= 23 && !other_field'
lttng enable-event -k --tracepoint sched_switch
lttng enable-event -k --tracepoint gpio_value
lttng enable-event -k --function usb_probe_device usb_probe_device
lttng enable-event -k --syscall --all
</pre>

The wildcard symbol, `*`, matches _anything_ and may only be used at
the end of the string when specifying a _tracepoint_. Make sure to
use it between single quotes in your favorite shell to avoid
undesired shell expansion.

System call events can be enabled individually, too:

<pre class="term">
lttng enable-event -k --syscall open
lttng enable-event -k --syscall read
lttng enable-event -k --syscall fork,chdir,pipe
</pre>

The complete list of available system call events can be
obtained using

<pre class="term">
lttng list --kernel --syscall
</pre>

You can see a list of events (enabled or disabled) using

<pre class="term">
lttng list some-session
</pre>

where `some-session` is the name of the desired tracing session.

What you're actually doing when enabling events with specific conditions
is creating a **whitelist** of traceable events for a given channel.
Thus, the following case presents redundancy:

<pre class="term">
lttng enable-event -u --tracepoint my_app:hello_you
lttng enable-event -u --tracepoint my_app:hello_you --loglevel TRACE_DEBUG
</pre>

The second command, matching a log level range, is useless since the first
command enables all tracepoints matching the same name,
`my_app:hello_you`.

Disabling an event is simpler: you only need to provide the event
name to the `disable-event` command:

<pre class="term">
lttng disable-event --userspace my_app:hello_you
</pre>

This name has to match a name previously given to `enable-event` (it
has to be listed in the output of `lttng list some-session`).
The `*` wildcard is supported, as long as you also used it in a
previous `enable-event` invocation.

Disabling an event does not add it to some blacklist: it simply removes
it from its channel's whitelist. This is why you cannot disable an event
which wasn't previously enabled.

A disabled event doesn't generate any trace data, even if all its
specified conditions are met.

Events may be enabled and disabled at will, either when LTTng tracers
are active or not. Events may be enabled before a user space application
is even started.
