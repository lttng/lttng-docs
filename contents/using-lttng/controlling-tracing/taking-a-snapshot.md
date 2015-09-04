---
id: taking-a-snapshot
---

The normal behavior of LTTng is to record trace data as trace files.
This is ideal for keeping a long history of events that occurred on
the target system and applications, but may be too much data in some
situations. For example, you may wish to trace your application
continuously until some critical situation happens, in which case you
would only need the latest few recorded events to perform the desired
analysis, not multi-gigabyte trace files.

LTTng has an interesting feature called _snapshots_. When creating
a tracing session in snapshot mode, no trace files are written; the
tracers' sub-buffers are constantly overwriting the oldest recorded
events with the newest. At any time, either when the tracers are started
or stopped, you may take a snapshot of those sub-buffers.

There is no difference between the format of a normal trace file and the
format of a snapshot: viewers of LTTng traces also support LTTng
snapshots. By default, snapshots are written to disk, but they may also
be sent over the network.

To create a tracing session in snapshot mode, do:

<pre class="term">
lttng create --snapshot my-snapshot-session
</pre>

Next, enable channels, events and add context to channels as usual.
Once a tracing session is created in snapshot mode, channels are
forced to use the
[overwrite](#doc-channel-overwrite-mode-vs-discard-mode) mode
(`--overwrite` option of the `enable-channel` command; also called
_flight recorder mode_) and have an `mmap()` channel type
(`--output mmap`).

Start tracing. When you're ready to take a snapshot, do:

<pre class="term">
lttng snapshot record --name my-snapshot
</pre>

This records a snapshot named `my-snapshot` of all channels of
all domains of the current tracing session. By default, snapshots files
are recorded in the path returned by `lttng snapshot list-output`. You
may change this path or decide to send snapshots over the network
using either:

  1. an output path/URL specified when creating the tracing session
     (`lttng create`)
  2. an added snapshot output path/URL using
     `lttng snapshot add-output`
  3. an output path/URL provided directly to the
     `lttng snapshot record` command

Method 3 overrides method 2 which overrides method 1. When specifying
a URL, a relay daemon must be listening on some machine (see
[Sending trace data over the network](#doc-sending-trace-data-over-the-network)).

If you need to make absolutely sure that the output file won't be
larger than a certain limit, you can set a maximum snapshot size when
taking it with the `--max-size` option:

<pre class="term">
lttng snapshot record --name my-snapshot --max-size 2M
</pre>

Older recorded events are discarded in order to respect this
maximum size.
