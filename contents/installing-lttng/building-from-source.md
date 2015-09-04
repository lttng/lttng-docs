---
id: building-from-source
---

As [previously stated](#doc-installing-lttng), LTTng is shipped as
three packages: LTTng-tools, LTTng-modules and LTTng-UST. LTTng-tools
contains everything needed to control tracing sessions, while
LTTng-modules is only needed for Linux kernel tracing and LTTng-UST is
only needed for user space tracing.

The tarballs are available in the
<a href="http://lttng.org/download#build-from-source" class="ext">Download
section</a> of the LTTng website.

Please refer to the `README.md` files provided by each package to
properly build and install them.

<div class="tip">
<p>
<span class="t">Tip:</span>The aforementioned <code>README.md</code> files
are rendered as rich text when
<a href="https://github.com/lttng" class="ext">viewed on GitHub</a>.
</p>
</div>

If you're using Ubuntu, executing the following Bash script
installs the appropriate dependencies, clones the LTTng
Git repositories, builds the projects, and installs them. The sources
are cloned into `~/src`. Your user needs to be a sudoer for the install
steps to be completed.

~~~ text
#!/bin/bash

mkdir ~/src
cd ~/src
sudo apt-get update
sudo apt-get -y install build-essential libtool flex bison \
                        libpopt-dev uuid-dev libglib2.0-dev autoconf \
                        git libxml2-dev
git clone git://git.lttng.org/lttng-ust.git
git clone git://git.lttng.org/lttng-modules.git
git clone git://git.lttng.org/lttng-tools.git
git clone git://git.lttng.org/userspace-rcu.git
git clone http://git.linuxfoundation.org/diamon/babeltrace.git

cd userspace-rcu
./bootstrap && ./configure && make -j 4 && sudo make install
sudo ldconfig

cd ../lttng-ust
./bootstrap && ./configure && make -j 4 && sudo make install
sudo ldconfig

cd ../lttng-modules
make && sudo make modules_install
sudo depmod -a

cd ../lttng-tools
./bootstrap && ./configure && make -j 4 && sudo make install
sudo ldconfig
sudo cp extras/lttng-bash_completion /etc/bash_completion.d/lttng

cd ../babeltrace
./bootstrap && ./configure && make -j 4 && sudo make install
sudo ldconfig
~~~
