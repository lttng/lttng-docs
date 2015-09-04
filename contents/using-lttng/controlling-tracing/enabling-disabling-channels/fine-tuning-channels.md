---
id: fine-tuning-channels
---

There are various parameters that may be fine-tuned with the
`enable-channel` command. The latter are well documented in
<a href="/man/1/lttng" class="ext">the man page of `lttng`</a>
and in the [Channel](#doc-channel) section of the
[Understanding LTTng](#doc-understanding-lttng) chapter. For basic
tracing needs, their default values should be just fine, but here are a
few examples to break the ice.

As the frequency of recorded events increases&mdash;either because the
event throughput is actually higher or because you enabled more events
than usual&mdash;_event loss_ might be experienced. Since LTTng never
waits, by design, for sub-buffer space availability (non-blocking
tracer), when a sub-buffer is full and no empty sub-buffers are left,
there are two possible outcomes: either the new events that do not fit
are rejected, or they start replacing the oldest recorded events.
The choice of which algorithm to use is a per-channel parameter, the
default being discarding the newest events until there is some space
left. If your situation always needs the latest events at the expense
of writing over the oldest ones, create a channel with the `--overwrite`
option:

<pre class="term">
lttng enable-channel --kernel --overwrite my-channel
</pre>

When an event is lost, it means no space was available in any
sub-buffer to accommodate it. Thus, if you want to cope with sporadic
high event throughput situations and avoid losing events, you need to
allocate more room for storing them in memory. This can be done by
either increasing the size of sub-buffers or by adding sub-buffers.
The following example creates a user space domain channel with
16&nbsp;sub-buffers of 512&nbsp;kiB each:

<pre class="term">
lttng enable-channel --userspace --num-subbuf 16 --subbuf-size 512k big-channel
</pre>

Both values need to be powers of two, otherwise they are rounded up
to the next one.

Two other interesting available parameters of `enable-channel` are
`--tracefile-size` and `--tracefile-count`, which respectively limit
the size of each trace file and the their count for a given channel.
When the number of written trace files reaches its limit for a given
channel-CPU pair, the next trace file overwrites the very first
one. The following example creates a kernel domain channel with a
maximum of three trace files of 1&nbsp;MiB each:

<pre class="term">
lttng enable-channel --kernel --tracefile-size 1M --tracefile-count 3 my-channel
</pre>

An efficient way to make sure lots of events are generated is enabling
all kernel events in this channel and starting the tracer:

<pre class="term">
lttng enable-event --kernel --all --channel my-channel
lttng start
</pre>

After a few seconds, look at trace files in your tracing session
output directory. For two CPUs, it should look like:

~~~ text
my-channel_0_0    my-channel_1_0
my-channel_0_1    my-channel_1_1
my-channel_0_2    my-channel_1_2
~~~

Amongst the files above, you might see one in each group with a size
lower than 1&nbsp;MiB: they are the files currently being written.

Since all those small files are valid LTTng trace files, LTTng trace
viewers may read them. It is the viewer's responsibility to properly
merge the streams so as to present an ordered list to the user.
<a href="http://www.efficios.com/babeltrace" class="ext">Babeltrace</a>
merges LTTng trace files correctly and is fast at doing it.
