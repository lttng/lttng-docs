---
id: opensuse
---

The openSUSE Leap 42.1 repository includes LTTng 2.7 packages.

Use `zypper` directly:

<pre class="term">
sudo zypper install lttng-tools
sudo zypper install lttng-modules
sudo zypper install lttng-ust-devel
</pre>

<div class="tip">
<p>
  <span class="t">Note:</span> If you need to trace Java
  applications on openSUSE, you need to build and install LTTng-UST 2.7
  <a href="#doc-building-from-source">from source</a> and use the
  <code>--enable-java-agent-jul</code>,
  <code>--enable-java-agent-log4j</code>, or
  <code>--enable-java-agent-all</code> options.
</p>
<p>
  If you need to trace Python applications on openSUSE, you need
  to build and install LTTng-UST 2.7 from source and use the
  <code>--enable-python-agent</code> option.
</p>
</div>
