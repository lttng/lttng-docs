---
id: liblttng-ctl-lttng
---

The LTTng control library, `liblttng-ctl`, can be used to communicate
with the session daemon using a C API that hides the underlying
protocol's details. `liblttng-ctl` is part of LTTng-tools.

`liblttng-ctl` may be used by including its "master" header:

~~~ c
#include <lttng/lttng.h>
~~~

Some objects are referred by name (C string), such as tracing sessions,
but most of them require creating a handle first using
`lttng_create_handle()`. The best available developer documentation for
`liblttng-ctl` is, for the moment, its installed header files as such.
Every function/structure is thoroughly documented.

The `lttng` program is the _de facto_ standard user interface to
control LTTng tracing sessions. `lttng` uses `liblttng-ctl` to
communicate with session daemons behind the scenes.
<a href="/man/1/lttng" class="ext">Its man page</a> is exhaustive, as
well as its command line help (<code>lttng <em>cmd</em> --help</code>,
where <code><em>cmd</em></code> is the command name).

The [Controlling tracing](#doc-controlling-tracing) section is a feature
tour of the `lttng` tool.
