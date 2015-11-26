---
id: archlinux
---

LTTng 2.7 packages are currently available in the
<abbr title="Arch User Repository">AUR</abbr> under the following names:
<a href="https://aur.archlinux.org/packages/lttng-tools/" class="ext"><code>lttng-tools</code></a>,
<a href="https://aur.archlinux.org/packages/lttng-modules/" class="ext"><code>lttng-modules</code></a>
and
<a href="https://aur.archlinux.org/packages/lttng-ust/" class="ext"><code>lttng-ust</code></a>.

The three LTTng packages can be installed using the following
<a href="https://wiki.archlinux.org/index.php/yaourt" class="ext">Yaourt</a> commands:

<pre class="term">
yaourt -S lttng-tools
yaourt -S lttng-modules
yaourt -S lttng-ust
</pre>

If you need to trace [Python applications](#doc-python-application), you
need to install the LTTng-UST Python agent also:

  * Python 3: <a href="https://aur.archlinux.org/packages/python-lttngust/" class="ext"><code>python-lttngust</code></a>
  * Python 2: <a href="https://aur.archlinux.org/packages/python2-lttngust/" class="ext"><code>python2-lttngust</code></a>

<div class="tip">
<p>
  <span class="t">Note:</span> If you need to trace
  <a href="#doc-java-application" class="int">Java</a>
  applications on Arch Linux, you need to build and install LTTng-UST 2.7
  <a href="#doc-building-from-source" class="int">from source</a> and
  use the <code>--enable-java-agent-jul</code>,
  <code>--enable-java-agent-log4j</code>, or
  <code>--enable-java-agent-all</code> options.
</p>
</div>
