---
id: lttng-ust-pkg-config
---

On some distributions, LTTng-UST is shipped with a pkg-config metadata
file, so that you may use the `pkg-config` tool:

<pre class="term">
pkg-config --libs lttng-ust
</pre>

This prints `-llttng-ust -ldl` on Linux systems.

You may also check the LTTng-UST version using `pkg-config`:

<pre class="term">
pkg-config --modversion lttng-ust
</pre>

For more information about pkg-config, see
<a href="http://linux.die.net/man/1/pkg-config" class="ext">its man page</a>.
