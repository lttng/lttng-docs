---
id: building-instrumented-32-bit-c-application
---

Let us reuse the _Hello world_ example of
[Tracing your own user application](#doc-tracing-your-own-user-application)
([Getting started](#doc-getting-started) chapter).

The instrumentation process is unaltered.

First, a typical 64-bit build (assuming you're running a 64-bit system):

<pre class="term">
gcc -o hello64 -I. hello.c hello-tp.c -ldl -llttng-ust
</pre>

Now, a 32-bit build:

<pre class="term">
gcc -o hello32 -I. <strong>-m32</strong> hello.c hello-tp.c <strong>-L/usr/lib32</strong> \
    -ldl -llttng-ust <strong>-Wl,-rpath,/usr/lib32</strong>
</pre>

The `-rpath` option, passed to the linker, makes the dynamic loader
check for libraries in `/usr/lib32` before looking in its default paths,
where it should find the 32-bit version of `liblttng-ust`.
