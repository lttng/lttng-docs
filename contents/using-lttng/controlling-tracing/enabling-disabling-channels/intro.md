---
id: enabling-disabling-channels
---

[As mentioned](#doc-event) in the
[Understanding LTTng](#doc-understanding-lttng) chapter, enabled
events are contained in a specific channel, itself contained in a
specific tracing session. A channel is a group of events with
tunable parameters (event loss mode, sub-buffer size, number of
sub-buffers, trace file sizes and count, to name a few). A given channel
may only be responsible for enabled events belonging to one domain:
either kernel or user space.

If you only used the `create`, `enable-event` and `start`/`stop`
commands of the `lttng` tool so far, one or two channels were
automatically created for you (one for the kernel domain and/or one
for the user space domain). The default channels are both named
`channel0`; channels from different domains may have the same name.

The current channels of a given tracing session can be viewed with

<pre class="term">
lttng list some-session
</pre>

where `some-session` is the name of the desired tracing session.

To create and enable a channel, use the `enable-channel` command:

<pre class="term">
lttng enable-channel --kernel my-channel
</pre>

This creates a kernel domain channel named `my-channel` with
default parameters in the current tracing session.

<div class="tip">
<p>
    <span class="t">Note:</span>Because of a current limitation, all
    channels must be <em>created</em> prior to beginning tracing in a
    given tracing session, that is before the first time you do
    <code>lttng start</code>.
</p>
<p>
    Since a channel is automatically created by
    <code>enable-event</code> only for the specified domain, you cannot,
    for example, enable a kernel domain event, start tracing and then
    enable a user space domain event because no user space channel
    exists yet and it's too late to create one.
</p>
<p>
    For this reason, make sure to configure your channels properly
    before starting the tracers for the first time!
</p>
</div>

Here's another example:

<pre class="term">
lttng enable-channel --userspace --session other-session --overwrite \
                     --tracefile-size 1048576 1mib-channel
</pre>

This creates a user space domain channel named `1mib-channel` in
the tracing session named `other-session` that loses new events by
overwriting previously recorded events (instead of the default mode of
discarding newer ones) and saves trace files with a maximum size of
1&nbsp;MiB each.

Note that channels may also be created using the `--channel` option of
the `enable-event` command when the provided channel name doesn't exist
for the specified domain:

<pre class="term">
lttng enable-event --kernel --channel some-channel sched_switch
</pre>

If no kernel domain channel named `some-channel` existed before calling
the above command, it would be created with default parameters.

You may enable the same event in two different channels:

<pre class="term">
lttng enable-event --userspace --channel my-channel app:tp
lttng enable-event --userspace --channel other-channel app:tp
</pre>

If both channels are enabled, the occurring `app:tp` event
generates two recorded events, one for each channel.

Disabling a channel is done with the `disable-event` command:

<pre class="term">
lttng disable-event --kernel some-channel
</pre>

The state of a channel precedes the individual states of events within
it: events belonging to a disabled channel, even if they are
enabled, won't be recorded.

