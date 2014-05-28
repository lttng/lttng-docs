---
id: cxx-application
---

Because of C++'s cross-compatibility with the C language, C++
applications can be readily instrumented with the LTTng-UST C API.

Follow the [C application](#doc-c-application) user guide above. It
should be noted that, in this case, tracepoint providers should have
the typical `.cpp`, `.cxx` or `.cc` extension and be built with `g++`
instead of `gcc`. This is the easiest way of avoiding linking errors
due to symbol name mangling incompatibilities between both languages.
