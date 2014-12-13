---
id: dynamic-linking
---

The second approach to package the tracepoint providers is to use
dynamic linking: the library and its member functions are explicitly
sought, loaded and unloaded at runtime using `libdl`.

It has to be noted that, for a variety of reasons, the created shared
library will be dynamically _loaded_, as opposed to dynamically
_linked_. The tracepoint provider shared object is, however, linked
with `liblttng-ust`, so that `liblttng-ust` is guaranteed to be loaded
as soon as the tracepoint provider is. If the tracepoint provider is
not loaded, since the application itself is not linked with
`liblttng-ust`, the latter is not loaded at all and the tracepoint calls
become inert.

The process to create the tracepoint provider shared object is pretty
much the same as the static library method, except that:

  * since the tracepoint provider is not part of the application
    anymore, `TRACEPOINT_DEFINE` _must_ be defined in one translation
    unit (C source file) of the _application_;
  * `TRACEPOINT_PROBE_DYNAMIC_LINKAGE` must be defined next to
    `TRACEPOINT_DEFINE`.

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
linked with the user application: it will be loaded manually. This is
why the application is built with no mention of this tracepoint
provider, but still needs `libdl`:

<pre class="term">
gcc -o app other.o files.o of.o your.o app.o <strong>-ldl</strong>
</pre>

Now, to make LTTng-UST tracing available to the application,
the `LD_PRELOAD` environment variable is used to preload the
tracepoint provider shared library _before_ the application actually
starts:

<pre class="term">
<strong>LD_PRELOAD=/path/to/tp.so</strong> ./app
</pre>

Your application will still work without this preloading, albeit without
LTTng-UST tracing support:

<pre class="term">
./app
</pre>
