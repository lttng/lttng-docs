---
id: creating-destroying-tracing-sessions
---

Whatever you want to do with `lttng`, it has to happen inside a
**tracing session**, created beforehand. A session, in general, is a
per-user container of state. A tracing session is no different; it
keeps a specific state of stuff like:

  * session name
  * enabled/disabled channels with associated parameters
  * enabled/disabled events with associated log levels and filters
  * context information added to channels
  * tracing activity (started or stopped)

and more.

A single user may have many active tracing sessions. LTTng session
daemons are the ultimate owners and managers of tracing sessions. For
user space tracing, each user has its own session daemon. Since Linux
kernel tracing requires root privileges, only `root`'s session daemon
may enable and trace  kernel events. However, `lttng` has a `--group`
option (which is passed to `lttng-sessiond` when starting it) to
specify the name of a _tracing group_ which selected users may be part
of to be allowed to communicate with `root`'s session daemon. By
default, the tracing group name is `tracing`.

To create a tracing session, do:

<pre class="term">
lttng create my-session
</pre>

This creates a new tracing session named `my-session` and make it
the current one. If you don't specify a name (running only
`lttng create`), your tracing session is named `auto` followed by the
current date and time. Traces
are written in <code>~/lttng-traces/<em>session</em>-</code> followed
by the tracing session's creation date/time by default, where
<code><em>session</em></code> is the tracing session name. To save them
at a different location, use the `--output` option:

<pre class="term">
lttng create --output /tmp/some-directory my-session
</pre>

You may create as many tracing sessions as you wish:

<pre class="term">
lttng create other-session
lttng create yet-another-session
</pre>

You may view all existing tracing sessions using the `list` command:

<pre class="term">
lttng list
</pre>

The state of a _current tracing session_ is kept in `~/.lttngrc`. Each
invocation of `lttng` reads this file to set its current tracing
session name so that you don't have to specify a session name for each
command. You could edit this file manually, but the preferred way to
set the current tracing session is to use the `set-session` command:

<pre class="term">
lttng set-session other-session
</pre>

Most `lttng` commands accept a `--session` option to specify the name
of the target tracing session.

Any existing tracing session may be destroyed using the `destroy`
command:

<pre class="term">
lttng destroy my-session
</pre>

Providing no argument to `lttng destroy` destroys the current
tracing session. Destroying a tracing session stops any tracing
running within the latter. Destroying a tracing session frees resources
acquired by the session daemon and tracer side, making sure to flush
all trace data.

You can't do much with LTTng using only the `create`, `set-session`
and `destroy` commands of `lttng`, but it is essential to know them in
order to control LTTng tracing, which always happen within the scope of
a tracing session.
