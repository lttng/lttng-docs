---
id: building-32-bit-userspace-rcu
---

Follow this:

<pre class="term">
git clone git://git.urcu.so/urcu.git
cd urcu
./bootstrap
./configure --libdir=/usr/lib32 CFLAGS=-m32
make
sudo make install
sudo ldconfig
</pre>

The `-m32` C compiler flag creates 32-bit object files and `--libdir`
indicates where to install the resulting libraries.
