---
id: pid-tracking
since: 2.7
---

It's often useful to allow only specific process IDs (PIDs) to emit
enabled events. For example, you may wish to record all the system
calls made by a given process (à la
<a href="http://linux.die.net/man/1/strace" class="ext">strace</a>).

The `lttng track` and `lttng untrack` commands serve this purpose. Both
commands operate on a whitelist of process IDs. The `track` command
adds entries to this whitelist while the `untrack` command removes
entries. Any process having one of the PIDs in the whitelist is allowed
to emit [enabled](#doc-enabling-disabling-events) LTTng events.

<div class="tip">
<p>
    <span class="t">Note:</span>The PID tracker tracks the
    <em>numeric process IDs</em>. Should a process with a given tracked
    ID exit and another process be given this ID, then the latter would
    also be allowed to emit events.
</p>
</div>

For the sake of the following examples, assume the target system has 16
possible PIDs. When a [tracing session](#doc-creating-destroying-tracing-sessions)
is created, the whitelist contains all the possible PIDs:

<figure class="img img-100">
<img src="/images/docs27/track-all.png" alt="All PIDs are tracked">
<figcaption>All PIDs are tracked</figcaption>
</figure>

When the whitelist is full and the `track` command is executed to specify
some PIDs to track, the whitelist is first cleared, then the specific
PIDs are tracked. For example, after

<pre class="term">
lttng track --pid 3,4,7,10,13
</pre>

the whitelist is:

<figure class="img img-100">
<img src="/images/docs27/track-3-4-7-10-13.png" alt="PIDs 3, 4, 7, 10, and 13 are tracked">
<figcaption>PIDs 3, 4, 7, 10, and 13 are tracked</figcaption>
</figure>

More PIDs can be added to the whitelist afterwards:

<pre class="term">
lttng track --pid 1,15,16
</pre>

gives:

<figure class="img img-100">
<img src="/images/docs27/track-1-3-4-7-10-13-15-16.png" alt="PIDs 1, 15, and 16 are added to the whitelist">
<figcaption>PIDs 1, 15, and 16 are added to the whitelist</figcaption>
</figure>

The `untrack` command removes entries from the PID tracker's whitelist.
Given the last example, the following command:

<pre class="term">
lttng untrack --pid 3,7,10,13
</pre>

leads to this whitelist:

<figure class="img img-100">
<img src="/images/docs27/track-1-4-15-16.png" alt="PIDs 3, 7, 10, and 13 are removed from the whitelist">
<figcaption>PIDs 3, 7, 10, and 13 are removed from the whitelist</figcaption>
</figure>

All possible PIDs can be tracked again using the `--all` option of
`lttng track`:

<pre class="term">
lttng track --pid --all
</pre>

gives:

<figure class="img img-100">
<img src="/images/docs27/track-all.png" alt="All PIDs are tracked">
<figcaption>All PIDs are tracked</figcaption>
</figure>

A very typical use case with PID tracking is starting with an empty
whitelist, then [starting the tracers](#doc-basic-tracing-session-control),
and then adding PIDs manually while tracing is active. This can be
accomplished by using the `--all` option of the `untrack` command
to clear the whitelist after a tracing session is created:

<pre class="term">
lttng untrack --pid --all
</pre>

gives:

<figure class="img img-100">
<img src="/images/docs27/untrack-all.png" alt="No PIDs are tracked">
<figcaption>No PIDs are tracked</figcaption>
</figure>

Tracing with this whitelist configuration does not produce any event
because no processes are tracked. The `track` command can be used
as usual to track specific PIDs, for example:

<pre class="term">
lttng track --pid 6,11
</pre>

results in:

<figure class="img img-100">
<img src="/images/docs27/track-6-11.png" alt="PIDs 6 and 11 are tracked">
<figcaption>PIDs 6 and 11 are tracked</figcaption>
</figure>
