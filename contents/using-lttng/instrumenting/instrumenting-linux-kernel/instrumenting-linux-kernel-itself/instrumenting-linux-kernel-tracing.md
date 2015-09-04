---
id: instrumenting-linux-kernel-tracing
---

The [Controlling tracing](#doc-controlling-tracing) section explains
how to use the `lttng` tool to create and control tracing sessions.
Although the `lttng` tool loads the appropriate _known_ LTTng kernel
modules when needed (by launching `root`'s session daemon), it won't
load your custom `lttng-probe-hello` module by default. You need to
manually start an LTTng session daemon as `root` and use the
`--extra-kmod-probes` option to append your custom probe module to the
default list:

<pre class="term">
sudo pkill -u root lttng-sessiond
sudo lttng-sessiond --extra-kmod-probes=hello
</pre>

The first command makes sure any existing instance is killed. If
you're not interested in using the default probes, or if you only
want to use a few of them, you could use `--kmod-probes` instead,
which specifies an absolute list:

<pre class="term">
sudo lttng-sessiond --kmod-probes=hello,ext4,net,block,signal,sched
</pre>

Confirm the custom probe module is loaded:

<pre class="term">
lsmod | grep lttng_probe_hello
</pre>

The `hello_world` event should appear in the list when doing

<pre class="term">
lttng list --kernel | grep hello
</pre>

You may now create an LTTng tracing session, enable the `hello_world`
kernel event (and others if you wish) and start tracing:

<pre class="term">
sudo lttng create my-session
sudo lttng enable-event --kernel hello_world
sudo lttng start
</pre>

Plug a few USB devices, then stop tracing and inspect the trace (if
<a href="http://www.efficios.com/babeltrace" class="ext">Babeltrace</a>
is installed):

<pre class="term">
sudo lttng stop
sudo lttng view
</pre>

Here's a sample output:

~~~ text
[15:30:34.835895035] (+?.?????????) hostname hello_world: { cpu_id = 1 }, { my_int = 8, char0 = 68, char1 = 97, product = "DataTraveler 2.0" }
[15:30:42.262781421] (+7.426886386) hostname hello_world: { cpu_id = 1 }, { my_int = 9, char0 = 80, char1 = 97, product = "Patriot Memory" }
[15:30:48.175621778] (+5.912840357) hostname hello_world: { cpu_id = 1 }, { my_int = 10, char0 = 68, char1 = 97, product = "DataTraveler 2.0" }
~~~

Two USB flash drives were used for this test.

You may change your LTTng custom probe, rebuild it and reload it at
any time when not tracing. Make sure you remove the old module
(either by killing the root LTTng session daemon which loaded the
module in the first place, or by using `modprobe --remove` directly)
before loading the updated one.
