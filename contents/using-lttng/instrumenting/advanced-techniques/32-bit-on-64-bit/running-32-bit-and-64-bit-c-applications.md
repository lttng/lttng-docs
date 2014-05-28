---
id: running-32-bit-and-64-bit-c-applications
---

Now, both 32-bit and 64-bit versions of the _Hello world_ example above
can be traced in the same tracing session. Use the `lttng` tool as usual
to create a tracing session and start tracing:

<pre class="term">
lttng create session-3264
lttng enable-event -u -a
./hello32
./hello64
lttng stop
</pre>

Use `lttng view` to verify both processes were
successfully traced.
