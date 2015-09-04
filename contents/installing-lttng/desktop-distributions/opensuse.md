---
id: opensuse
---

openSUSE has had LTTng packages since version 12.3. To install LTTng, you
first need to add an entry to your repository configuration. All LTTng repositories
are available
<a href="http://download.opensuse.org/repositories/devel:/tools:/lttng/" class="ext">here</a>.
For example, the following commands adds the LTTng repository for
openSUSE&nbsp;13.1:

<pre class="term">
sudo zypper addrepo http://download.opensuse.org/repositories/devel:/tools:/lttng/openSUSE_13.1/devel:tools:lttng.repo
</pre>

Then, refresh the package database:

<pre class="term">
sudo zypper refresh
</pre>

and install `lttng-tools`, `lttng-modules` and `lttng-ust-devel`:

<pre class="term">
sudo zypper install lttng-tools
sudo zypper install lttng-modules
sudo zypper install lttng-ust-devel
</pre>
