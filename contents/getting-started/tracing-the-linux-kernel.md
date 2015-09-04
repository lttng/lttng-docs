---
id: tracing-the-linux-kernel
---

Make sure LTTng-tools and LTTng-modules packages
[are installed](#doc-installing-lttng).

Since you're about to trace the Linux kernel itself, let's look at the
available kernel events using the `lttng` tool, which has a
Git-like command line structure:

<pre class="term">
lttng list --kernel
</pre>

Before tracing, you need to create a session:

<pre class="term">
sudo lttng create
</pre>

<div class="tip">
<p>
    <span class="t">Tip:</span>You can avoid using <code>sudo</code> in
    the previous and following commands if your user is a member of the
    <a href="#doc-lttng-sessiond" class="int"><code>tracing</code>
    group</a>.
</p>
</div>

Let's now enable some events for this session:

<pre class="term">
sudo lttng enable-event --kernel sched_switch,sched_process_fork
</pre>

Or you might want to simply enable all available kernel events (beware
that trace files grow rapidly when doing this):

<pre class="term">
sudo lttng enable-event --kernel --all
</pre>

Start tracing:

<pre class="term">
sudo lttng start
</pre>

By default, traces are saved in
<code>~/lttng-traces/<em>name</em>-<em>date</em>-<em>time</em></code>,
where <code><em>name</em></code> is the session name.

When you're done tracing:

<pre class="term">
sudo lttng stop
sudo lttng destroy
</pre>

Although `destroy` looks scary here, it doesn't actually destroy the
written trace files: it only destroys the tracing session.

What's next? Have a look at
[Viewing and analyzing your traces](#doc-viewing-and-analyzing-your-traces)
to view and analyze the trace you just recorded.
