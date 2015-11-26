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

If you need to trace Python applications, you need to install the
LTTng-UST Python agent also:

  * Python 3: <a href="https://aur.archlinux.org/packages/python-lttngust/" class="ext"><code>python-lttngust</code></a>
  * Python 2: <a href="https://aur.archlinux.org/packages/python2-lttngust/" class="ext"><code>python2-lttngust</code></a>
