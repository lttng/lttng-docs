---
id: lttng-ust-environment-variables-compiler-flags
---

A few special environment variables and compile flags may affect the
behavior of LTTng-UST.

LTTng-UST's debugging can be activated by setting the environment
variable `LTTNG_UST_DEBUG` to `1` when launching the application. It
can also be enabled at compile time by defining `LTTNG_UST_DEBUG` when
compiling LTTng-UST (using the `-DLTTNG_UST_DEBUG` compiler option).

The environment variable `LTTNG_UST_REGISTER_TIMEOUT` can be used to
specify how long the application should wait for the
[session daemon](#doc-lttng-sessiond)'s _registration done_ command
before proceeding to execute the main program. The timeout value is
specified in milliseconds. 0 means _don't wait_. -1 means
_wait forever_. Setting this environment variable to 0 is recommended
for applications with time contraints on the process startup time.

The default value of `LTTNG_UST_REGISTER_TIMEOUT` (when not defined)
is **3000&nbsp;ms**.

The compilation definition `LTTNG_UST_DEBUG_VALGRIND` should be enabled
at build time (`-DLTTNG_UST_DEBUG_VALGRIND`) to allow `liblttng-ust`
to be used with <a href="http://valgrind.org/" class="ext">Valgrind</a>.
The side effect of defining `LTTNG_UST_DEBUG_VALGRIND` is that per-CPU
buffering is disabled.
