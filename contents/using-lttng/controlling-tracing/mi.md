---
id: mi
since: 2.6
---

The `lttng` tool aims at providing a command output as human-readable as
possible. While this output is easy to parse by a human being, machines
have a hard time.

This is why the `lttng` tool provides the general `--mi` option, which
must specify a machine interface output format. As of the latest
LTTng stable release, only the `xml` format is supported. A schema
definition (XSD) is made
<a href="https://github.com/lttng/lttng-tools/blob/master/src/common/mi_lttng.xsd" class="ext">available</a>
to ease the integration with external tools as much as possible.

The `--mi` option can be used in conjunction with all `lttng` commands.
Here are some examples:

<pre class="term">
lttng --mi xml create some-session
lttng --mi xml list some-session
lttng --mi xml list --kernel
lttng --mi xml enable-event --kernel --syscall open
lttng --mi xml start
</pre>
