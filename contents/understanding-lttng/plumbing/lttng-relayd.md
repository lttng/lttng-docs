---
id: lttng-relayd
---

When a tracing session is configured to send its trace data over the
network, an LTTng _relay daemon_ must be used at the other end to
receive trace packets and serialize them to trace files. This setup
makes it possible to trace a target system without ever committing trace
data to its local storage, a feature which is useful for embedded
systems, amongst others. The command implementing the relay daemon
is `lttng-relayd`.

The basic use case of `lttng-relayd` is to transfer trace data received
over the network to trace files on the local file system. The relay
daemon must listen on two TCP ports to achieve this: one control port,
used by the target session daemon, and one data port, used by the
target consumer daemon. The relay and session daemons agree on common
default ports when custom ones are not specified.

Since the communication transport protocol for both ports is standard
TCP, the relay daemon may be started either remotely or locally (on the
target system).

While two instances of consumer daemons (32-bit and 64-bit) may run
concurrently for a given user, `lttng-relayd` needs only be of its
host operating system's bitness.

The other important feature of LTTng's relay daemon is the support of
_LTTng live_. LTTng live is an application protocol to view events as
they arrive. The relay daemon still records events in trace files,
but a _tee_ allows to inspect incoming events.

<figure class="img img-100">
<img src="/images/docs26/lttng-live.png" alt="LTTng live">
<figcaption>
    The relay daemon creates a <em>tee</em>, forwarding the trace data
    to both trace files and a live viewer.
</figcaption>
</figure>

Using LTTng live
locally thus requires to run a local relay daemon.
