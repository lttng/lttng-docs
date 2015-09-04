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

`-L/usr/lib32` is required for the build to find the 32-bit versions
of Userspace RCU and other dependencies.

<div class="tip">
<p>
    <span class="t">Note:</span>Depending on your Linux distribution,
    32-bit libraries could be installed at a different location than
    <code>/usr/lib32</code>. For example, Debian is known to install
    some 32-bit libraries in <code>/usr/lib/i386-linux-gnu</code>.
</p>
<p>
    In this case, make sure to set <code>LDFLAGS</code> to all the
    relevant 32-bit library paths, for example,
    <code>LDFLAGS="-L/usr/lib32 -L/usr/lib/i386-linux-gnu"</code>.
</p>
</div>

<div class="tip">
<p>
    <span class="t">Note:</span>You may add options to
    <code>./configure</code> if you need them (for
    Java and SystemTap support, for example). Look at
    <code>./configure --help</code> for more information.
</p>
</div>
