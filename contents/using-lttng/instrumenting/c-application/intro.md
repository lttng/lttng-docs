---
id: c-application
---

Instrumenting a C (or C++) application, be it an executable program or
a library, implies using LTTng-UST, the
user space tracing component of LTTng. For C/C++ applications, the
LTTng-UST package includes a dynamically loaded library
(`liblttng-ust`), C headers and the `lttng-gen-tp` command line utility.

Since C and C++ are the base languages of virtually all other
programming languages
(Java virtual machine, Python, Perl, PHP and Node.js interpreters, to
name a few), implementing user space tracing for an unsupported language
is just a matter of using the LTTng-UST C API at the right places.

The usual work flow to instrument a user space C application with
LTTng-UST is:

  1. Define tracepoints (actual probes)
  2. Write tracepoint providers
  3. Insert tracepoints into target source code
  4. Package (build) tracepoint providers
  5. Build user application and link it with tracepoint providers

The steps above are discussed in greater detail in the following
subsections.
