---
id: lttng-ust
---

The user space tracing part of LTTng is possible thanks to the user
space tracing library, `liblttng-ust`, which is part of the LTTng-UST
package.

`liblttng-ust` provides header files containing macros used to define
tracepoints and create tracepoint providers, as well as a shared object
that must be linked to individual applications to connect to and
communicate with a session daemon and a consumer daemon as soon as the
application starts.

The exact mechanism by which an application is registered to the
session daemon is beyond the scope of this documentation. The only thing
you need to know is that, since the library constructor does this job
automatically, tracepoints may be safely inserted anywhere in the source
code without prior manual initialization of `liblttng-ust`.

The `liblttng-ust`-session daemon collaboration also provides an
interesting feature: user space events may be enabled _before_
applications actually start. By doing this and starting tracing before
launching the instrumented application, you make sure that even the
earliest occurring events can be recorded.

The [C application](#doc-c-application) instrumenting guide of the
[Using LTTng](#doc-using-lttng) chapter focuses on using `liblttng-ust`:
instrumenting, building/linking and running a user application.
