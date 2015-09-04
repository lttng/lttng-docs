---
id: building-64-bit-lttng-tools
---

Finally, you need to build a 64-bit version of LTTng-tools which is
aware of the 32-bit consumer daemon previously built and installed:

<pre class="term">
make clean
./bootstrap
./configure --prefix=/usr \
            --with-consumerd32-libdir=/usr/lib32 \
            --with-consumerd32-bin=/usr/lib32/lttng/libexec/lttng-consumerd
make
sudo make install
sudo ldconfig
</pre>

Henceforth, the 64-bit session daemon automatically finds the
32-bit consumer daemon if required.
