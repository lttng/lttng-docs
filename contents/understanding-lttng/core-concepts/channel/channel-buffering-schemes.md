---
id: channel-buffering-schemes
---

In the user space tracing domain, two **buffering schemes** are
available when creating a channel:

  * **Per-PID buffering**: keep one ring buffer per process.
  * **Per-UID buffering**: keep one ring buffer for all processes of
    a single user.

The per-PID buffering scheme consumes more memory than the per-UID
option if more than one process is instrumented for LTTng-UST. However,
per-PID buffering ensures that one process having a high event
throughput won't fill all the shared sub-buffers, only its own.

The Linux kernel tracing domain only has one available buffering scheme
which is to use a single ring buffer for the whole system.
