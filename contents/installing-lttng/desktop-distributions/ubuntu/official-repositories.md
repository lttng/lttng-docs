---
id: ubuntu-official-repositories
---

To install LTTng 2.7 from the official Ubuntu 16.04 _Xenial Xerus_
repositories, simply use `apt-get`:

<pre class="term">
sudo apt-get install lttng-tools
sudo apt-get install lttng-modules-dkms
sudo apt-get install liblttng-ust-dev
</pre>

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
