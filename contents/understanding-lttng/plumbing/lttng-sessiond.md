---
id: lttng-sessiond
---

At the heart of LTTng's plumbing is the _session daemon_, often called
by its command name, `lttng-sessiond`.

The session daemon is responsible for managing tracing sessions and
what they logically contain (channel properties, enabled/disabled
events, etc.). By communicating locally with instrumented applications
(using LTTng-UST) and with the LTTng Linux kernel modules
(LTTng-modules), it oversees all tracing activities.

One of the many things that `lttng-sessiond` does is to keep
track of the available event types. User space applications and
libraries actively connect and register to the session daemon when they
start. By contrast, `lttng-sessiond` seeks out and loads the appropriate
LTTng kernel modules as part of its own initialization. Kernel event
types are _pulled_ by `lttng-sessiond`, whereas user space event types
are _pushed_ to it by the various user space tracepoint providers.

Using a specific inter-process communication protocol with Linux kernel
and user space tracers, the session daemon can send channel information
so that they are initialized, enable/disable specific probes based on
enabled/disabled events by the user, send event filters information to
LTTng tracers so that filtering actually happens at the tracer site,
start/stop tracing a specific application or the Linux kernel, etc.

The session daemon is not useful without some user controlling it,
because it's only a sophisticated control interchange and thus
doesn't make any decision on its own. `lttng-sessiond` opens a local
socket for controlling it, albeit the preferred way to control it is
using `liblttng-ctl`, an installed C library hiding the communication
protocol behind an easy-to-use API. The `lttng` tool makes use of
`liblttng-ctl` to implement a user-friendly command line interface.

`lttng-sessiond` does not receive any trace data from instrumented
applications; the _consumer daemons_ are the programs responsible for
collecting trace data using shared ring buffers. However, the session
daemon is the one that must spawn a consumer daemon and establish
a control communication with it.

Session daemons run on a per-user basis. Knowing this, multiple
instances of `lttng-sessiond` may run simultaneously, each belonging
to a different user and each operating independently of the others.
Only `root`'s session daemon, however, may control LTTng kernel modules
(i.e. the kernel tracer). With that in mind, if a user has no root
access on the target system, he cannot trace the system's kernel, but
should still be able to trace its own instrumented applications.

It has to be noted that, although only `root`'s session daemon may
control the kernel tracer, the `lttng-sessiond` command has a `--group`
option which may be used to specify the name of a special user group
allowed to communicate with `root`'s session daemon and thus record
kernel traces. By default, this group is named `tracing`.

If not done yet, the `lttng` tool, by default, automatically starts a
session daemon. `lttng-sessiond` may also be started manually:

<pre class="term">
lttng-sessiond
</pre>

This starts the session daemon in foreground. Use

<pre class="term">
lttng-sessiond --daemonize
</pre>

to start it as a true daemon.

To kill the current user's session daemon, `pkill` may be used:

<pre class="term">
pkill lttng-sessiond
</pre>

The default `SIGTERM` signal terminates it cleanly.

Several other options are available and described in
<a href="/man/8/lttng-sessiond" class="ext"><code>lttng-sessiond</code>'s manpage</a>
or by running `lttng-sessiond --help`.
