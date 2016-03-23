---
id: persistent-memory-file-systems
since: 2.7
---

<a href="https://en.wikipedia.org/wiki/Non-volatile_random-access_memory" class="ext">Non-volatile random-access memory</a>
(NVRAM) is random-access memory that retains its information when power is turned off (non-volatile).
Systems with such memory can store data structures in RAM
and retrieve them after a reboot, without flushing to typical _storage_.

Linux supports NVRAM file systems thanks to either
<a href="http://pramfs.sourceforge.net/" class="ext">PRAMFS</a> or
<a href="https://www.kernel.org/doc/Documentation/filesystems/dax.txt" class="ext">DAX</a>&nbsp;+&nbsp;<a href="http://lkml.iu.edu/hypermail/linux/kernel/1504.1/03463.html" class="ext">pmem</a>
(requires Linux 4.1+).

This documentation does not describe how to operate such file systems;
it is assumed that you have a working persistent memory file system.

When creating an LTTng tracing session, you can use the `--shm-path`
option to specify the path of the shared memory holding the ring
buffers. Specifying a location on an NVRAM file system makes it possible
to retrieve the latest recorded trace data when the system reboots
after a crash.

Example:

<pre class="term">
lttng create <strong>--shm-path /path/to/shm</strong>
</pre>

The binary layout of the ring buffer files is not exactly the same as
the trace files layout. To view the events of ring buffer files after
a system crash, use the `lttng-crash` utility:

<pre class="term">
lttng-crash /path/to/shm
</pre>

This extracts the trace data behind the scenes and runs
<a href="http://diamon.org/babeltrace" class="ext"><code>babeltrace</code></a>
to view the events. To extract the trace data to an LTTng trace without
viewing the events, use the `--extract` option:

<pre class="term">
lttng-crash <strong>--extract /path/to/trace</strong> /path/to/shm
</pre>

See the <a href="/man/1/lttng-crash/v2.7" class="ext"><code>lttng-crash</code> man page</a>
for the complete list of options.
