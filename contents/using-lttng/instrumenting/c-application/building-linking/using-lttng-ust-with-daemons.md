---
id: using-lttng-ust-with-daemons
---

Some extra care is needed when using `liblttng-ust` with daemon
applications that call `fork()`, `clone()` or BSD's `rfork()` without
a following `exec()` family system call. The `liblttng-ust-fork`
library must be preloaded for the application.

Example:

<pre class="term">
<strong>LD_PRELOAD=liblttng-ust-fork.so</strong> ./app
</pre>

Or, if you're using a tracepoint provider shared library:

<pre class="term">
<strong>LD_PRELOAD="liblttng-ust-fork.so /path/to/tp.so"</strong> ./app
</pre>
