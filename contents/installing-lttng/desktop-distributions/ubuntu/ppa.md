---
id: ubuntu-ppa
---

The
<a href="https://launchpad.net/~lttng/+archive/ubuntu/ppa/" class="ext">LTTng latest stable PPA</a>
offers the latest stable LTTng 2.7 packages. To get packages from the
PPA, follow these steps:

<pre class="term">
sudo apt-add-repository ppa:lttng/ppa
sudo apt-get update
sudo apt-get install lttng-tools
sudo apt-get install lttng-modules-dkms
sudo apt-get install liblttng-ust-dev
sudo apt-get install liblttng-ust-agent-java
sudo apt-get install python3-lttngust
</pre>
