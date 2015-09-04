---
id: building-tracepoint-providers-and-user-application
---

This section explains the final step of using LTTng-UST for tracing
a user space C application (beside running the application): building and
linking tracepoint providers and the application itself.

As discussed above, the macros used by the user-written tracepoint provider
header file are useless until actually used to create probes code
(global data structures and functions) in a translation unit (C source file).
This is accomplished by defining `TRACEPOINT_CREATE_PROBES` in a translation
unit and then including the tracepoint provider header file.
When `TRACEPOINT_CREATE_PROBES` is defined, macros used and included by
the tracepoint provider header produce actual source code needed by any
application using the defined tracepoints. Defining
`TRACEPOINT_CREATE_PROBES` produces code used when registering
tracepoint providers when the tracepoint provider package loads.

The other important definition is `TRACEPOINT_DEFINE`. This one creates
global, per-tracepoint structures referencing the tracepoint providers
data. Those structures are required by the actual functions inserted
where `tracepoint()` macros are placed and need to be defined by the
instrumented application.

Both `TRACEPOINT_CREATE_PROBES` and `TRACEPOINT_DEFINE` need to be defined
at some places in order to trace a user space C application using LTTng.
Although explaining their exact mechanism is beyond the scope of this
document, the reason they both exist separately is to allow the trace
providers to be packaged as a shared object (dynamically loaded library).

There are two ways to compile and link the tracepoint providers
with the application: _[statically](#doc-static-linking)_ or
_[dynamically](#doc-dynamic-linking)_. Both methods are covered in the
following subsections.
