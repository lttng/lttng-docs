---
id: debian
---

Debian "stretch" and Debian "sid" have LTTng-modules 2.7 and
LTTng-UST 2.7 packages:

<pre class="term">
sudo apt-get install lttng-modules-dkms
sudo apt-get install liblttng-ust-dev
</pre>

LTTng-tools 2.7 still needs to be
[built from source](#doc-building-from-source).

If you need to trace [Java applications](#doc-java-application), you
need to install the LTTng-UST Java agent also:

<pre class="term">
sudo apt-get install liblttng-ust-agent-java
</pre>

If you need to trace [Python applications](#doc-python-application),
you need to install the LTTng-UST Python agent also:

<pre class="term">
sudo apt-get install python3-lttngust
</pre>
