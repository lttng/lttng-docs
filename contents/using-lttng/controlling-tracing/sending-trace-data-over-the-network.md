---
id: sending-trace-data-over-the-network
---

The possibility of sending trace data over the network comes as a
built-in feature of LTTng-tools. For this to be possible, an LTTng
_relay daemon_ must be executed and listening on the machine where
trace data is to be received, and the user must create a tracing
session using appropriate options to forward trace data to the remote
relay daemon.

The relay daemon listens on two different TCP ports: one for control
information and the other for actual trace data.

Starting the relay daemon on the remote machine is easy:

<pre class="term">
lttng-relayd
</pre>

This makes it listen to its default ports: 5342 for control and
5343 for trace data. The `--control-port` and `--data-port` options may
be used to specify different ports.

Traces written by `lttng-relayd` are written to
<code>~/lttng-traces/<em>hostname</em>/<em>session</em></code> by
default, where <code><em>hostname</em></code> is the host name of the
traced (monitored) system and <code><em>session</em></code> is the
tracing session name. Use the `--output` option to write trace data
outside `~/lttng-traces`.

On the sending side, a tracing session must be created using the
`lttng` tool with the `--set-url` option to connect to the distant
relay daemon:

<pre class="term">
lttng create my-session --set-url net://distant-host
</pre>

The URL format is described in the output of `lttng create --help`.
The above example uses the default ports; the `--ctrl-url` and
`--data-url` options may be used to set the control and data URLs
individually.

Once this basic setup is completed and the connection is established,
you may use the `lttng` tool on the target machine as usual; everything
you do is transparently forwarded to the remote machine if needed.
For example, a parameter changing the maximum size of trace files
only has an effect on the distant relay daemon actually writing
the trace.
