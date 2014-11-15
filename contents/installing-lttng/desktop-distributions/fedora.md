---
id: fedora
---

Starting from Fedora 17, LTTng-tools and LTTng-UST packages are officially
available using `yum`:

<pre class="term">
sudo yum install lttng-tools
sudo yum install lttng-ust
sudo yum install lttng-ust-devel
</pre>

LTTng-modules still needs to be built and installed from source. For that, 
make sure that the `kernel-devel` package is already installed beforehand:

<pre class="term">
sudo yum install kernel-devel
</pre>

Proceed on to fetch [LTTng-modules' source](#doc-building-from-source).
Build and install it as follows:

<pre class="term">
KERNELDIR=/usr/src/kernels/$(uname -r) make
sudo make modules_install
</pre>
