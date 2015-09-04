---
id: building-32-bit-lttng-tools
---

Since the host is a 64-bit system, most 32-bit binaries and libraries of
LTTng-tools are not needed; the host uses their 64-bit counterparts.
The required step here is building and installing a 32-bit consumer
daemon.

Follow this:

<pre class="term">
git clone http://git.lttng.org/lttng-tools.git
cd lttng-ust
./bootstrap
./configure --prefix=/usr \
            --libdir=/usr/lib32 CFLAGS=-m32 CXXFLAGS=-m32 \
            LDFLAGS=-L/usr/lib32
make
cd src/bin/lttng-consumerd
sudo make install
sudo ldconfig
</pre>

The above commands build all the LTTng-tools project as 32-bit
applications, but only installs the 32-bit consumer daemon.
