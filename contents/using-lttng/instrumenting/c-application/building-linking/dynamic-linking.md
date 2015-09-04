---
id: dynamic-linking
---

The second approach to package the tracepoint providers is to use
dynamic linking: the library and its member functions are explicitly
sought, loaded and unloaded at runtime using `libdl`.

It has to be noted that, for a variety of reasons, the created shared
library is be dynamically _loaded_, as opposed to dynamically
_linked_. The tracepoint provider shared object is, however, linked
with `liblttng-ust`, so that `liblttng-ust` is guaranteed to be loaded
as soon as the tracepoint provider is. If the tracepoint provider is
not loaded, since the application itself is not linked with
`liblttng-ust`, the latter is not loaded at all and the tracepoint calls
become inert.

The process to create the tracepoint provider shared object is pretty
much the same as the static library method, except that:

  * since the tracepoint provider is not part of the application
    anymore, `TRACEPOINT_DEFINE` _must_ be defined, for each tracepoint
    provider, in exactly one translation unit (C source file) of the
    _application_;
  * `TRACEPOINT_PROBE_DYNAMIC_LINKAGE` must be defined next to
    `TRACEPOINT_DEFINE`.

Regarding `TRACEPOINT_DEFINE` and `TRACEPOINT_PROBE_DYNAMIC_LINKAGE`,
the recommended practice is to use a separate C source file in your
application to define them, and then include the tracepoint provider
header files afterwards, e.g.:

~~~ c
#define TRACEPOINT_DEFINE
#define TRACEPOINT_PROBE_DYNAMIC_LINKAGE

/* include the header files of one or more tracepoint providers below */
#include "tp1.h"
#include "tp2.h"
#include "tp3.h"
~~~

`TRACEPOINT_PROBE_DYNAMIC_LINKAGE` makes the macros included afterwards
(by including the tracepoint provider header, which itself includes
LTTng-UST headers) aware that the tracepoint provider is to be loaded
dynamically and not part of the application's executable.

The tracepoint provider object file used to create the shared library
is built like it is using the static library method, only with the
`-fpic` option added:

<pre class="term">
gcc -c <strong>-fpic</strong> -I. tp.c
</pre>

It is then linked as a shared library like this:

<pre class="term">
gcc <strong>-shared -Wl,--no-as-needed -o tp.so -llttng-ust</strong> tp.o
</pre>

As previously stated, this tracepoint provider shared object isn't
linked with the user application: it's loaded manually. This is
why the application is built with no mention of this tracepoint
provider, but still needs `libdl`:

<pre class="term">
gcc -o app other.o files.o of.o your.o app.o <strong>-ldl</strong>
</pre>

Now, to make LTTng-UST tracing available to the application, the
`LD_PRELOAD` environment variable is used to preload the tracepoint
provider shared library _before_ the application actually starts:

<pre class="term">
<strong>LD_PRELOAD=/path/to/tp.so</strong> ./app
</pre>

<div class="tip">
<p>
    <span class="t">Note:</span>It is not safe to use
    <code>dlclose()</code> on a tracepoint provider shared object that
    is being actively used for tracing, due to a lack of reference
    counting from LTTng-UST to the shared object.
</p>

<p>
    For example, statically linking a tracepoint provider to a
    shared object which is to be dynamically loaded by an application
    (e.g., a plugin) is not safe: the shared object, which contains the
    tracepoint provider, could be dynamically closed
    (<code>dlclose()</code>) at any time by the application.
</p>

<p>
    To instrument a shared object, either:
</p>

<ol>
    <li>
        Statically link the tracepoint provider to the
        <em>application</em>, or
    </li>
    <li>
        Build the tracepoint provider as a shared object (following
        the procedure shown in this section), and preload it when
        tracing is needed using the <code>LD_PRELOAD</code>
        environment variable.
    </li>
</ol>
</div>

Your application will still work without this preloading, albeit without
LTTng-UST tracing support:

<pre class="term">
./app
</pre>

