---
id: building-32-bit-lttng-ust
---

Follow this:

<pre class="term">
git clone http://git.lttng.org/lttng-ust.git
cd lttng-ust
./bootstrap
./configure --prefix=/usr \
            --libdir=/usr/lib32 \
            CFLAGS=-m32 CXXFLAGS=-m32 \
            LDFLAGS=-L/usr/lib32
make
sudo make install
sudo ldconfig
</pre>

`-L/usr/lib32` is required for the build to find the 32-bit version
of Userspace RCU.

<div class="tip">
<p>
    <span class="t">Note:</span>You may add options to
    <code>./configure</code> if you need them, e.g., for
    Java and SystemTap support. Look at
    <code>./configure --help</code> for more information.
</p>
</div>
