---
id: proc-lttng-logger-abi
since: 2.5
---

The `lttng-tracer` Linux kernel module, installed by the LTTng-modules
package, creates a special LTTng logger ABI file `/proc/lttng-logger`
when loaded. Writing text data to this file generates an LTTng kernel
domain event named `lttng_logger`.

Unlike other kernel domain events, `lttng_logger` may be enabled by
any user, not only root users or members of the tracing group.

To use the LTTng logger ABI, simply write a string to
`/proc/lttng-logger`:

<pre class="term">
echo -n 'Hello, World!' > /proc/lttng-logger
</pre>

The `msg` field of the `lttng_logger` event contains the recorded
message.

<div class="tip">
<p>
    <span class="t">Note:</span>Messages are split in chunks of
    1024&nbsp;bytes.
</p>
</div>

The LTTng logger ABI is a quick and easy way to trace some events from
user space through the kernel tracer. However, it is much more basic
than LTTng-UST: it's slower (involves system call round-trip to the
kernel and only supports logging strings). The LTTng logger ABI is
particularly useful for recording logs as LTTng traces from shell
scripts, potentially combining them with other Linux kernel/user space
events.
