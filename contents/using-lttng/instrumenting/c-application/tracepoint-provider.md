---
id: tracepoint-provider
---

Before jumping into defining tracepoints and inserting
them into the application source code, you must understand what a
_tracepoint provider_ is.

For the sake of this guide, consider the following two files:

`tp.h`:

~~~ c
#undef TRACEPOINT_PROVIDER
#define TRACEPOINT_PROVIDER my_provider

#undef TRACEPOINT_INCLUDE
#define TRACEPOINT_INCLUDE "./tp.h"

#if !defined(_TP_H) || defined(TRACEPOINT_HEADER_MULTI_READ)
#define _TP_H

#include <lttng/tracepoint.h>

TRACEPOINT_EVENT(
    my_provider,
    my_first_tracepoint,
    TP_ARGS(
        int, my_integer_arg,
        char*, my_string_arg
    ),
    TP_FIELDS(
        ctf_string(my_string_field, my_string_arg)
        ctf_integer(int, my_integer_field, my_integer_arg)
    )
)

TRACEPOINT_EVENT(
    my_provider,
    my_other_tracepoint,
    TP_ARGS(
        int, my_int
    ),
    TP_FIELDS(
        ctf_integer(int, some_field, my_int)
    )
)

#endif /* _TP_H */

#include <lttng/tracepoint-event.h>
~~~

`tp.c`:

~~~ c
#define TRACEPOINT_CREATE_PROBES

#include "tp.h"
~~~

The two files above are defining a _tracepoint provider_. A tracepoint
provider is some sort of namespace for _tracepoint definitions_. Tracepoint
definitions are written above with the `TRACEPOINT_EVENT()` macro, and allow
eventual `tracepoint()` calls respecting their definitions to be inserted
into the user application's C source code (we explore this in a
later section).

Many tracepoint definitions may be part of the same tracepoint provider
and many tracepoint providers may coexist in a user space application. A
tracepoint provider is packaged either:

  * directly into an existing user application's C source file
  * as an object file
  * as a static library
  * as a shared library

The two files above, `tp.h` and `tp.c`, show a typical template for
writing a tracepoint provider. LTTng-UST was designed so that two
tracepoint providers should not be defined in the same header file.

We will now go through the various parts of the above files and
give them a meaning. As you may have noticed, the LTTng-UST API for
C/C++ applications is some preprocessor sorcery. The LTTng-UST macros
used in your application and those in the LTTng-UST headers are
combined to produce actual source code needed to make tracing possible
using LTTng.

Let's start with the header file, `tp.h`. It begins with

~~~ c
#undef TRACEPOINT_PROVIDER
#define TRACEPOINT_PROVIDER my_provider
~~~

`TRACEPOINT_PROVIDER` defines the name of the provider to which the
following tracepoint definitions belong. It is used internally by
LTTng-UST headers and _must_ be defined. Since `TRACEPOINT_PROVIDER`
could have been defined by another header file also included by the same
C source file, the best practice is to undefine it first.

<div class="tip">
<p><span class="t">Note:</span>Names in LTTng-UST follow the C
<em>identifier</em> syntax (starting with a letter and containing either
letters, numbers or underscores); they are <em>not</em> C strings
(not surrounded by double quotes). This is because LTTng-UST macros
use those identifier-like strings to create symbols (named types and
variables).</p>
</div>

The tracepoint provider is a group of tracepoint definitions; its chosen
name should reflect this. A hierarchy like Java packages is recommended,
using underscores instead of dots, e.g., `org_company_project_component`.

Next is `TRACEPOINT_INCLUDE`:

~~~ c
#undef TRACEPOINT_INCLUDE
#define TRACEPOINT_INCLUDE "./tp.h"
~~~

This little bit of instrospection is needed by LTTng-UST to include
your header at various predefined places.

Include guard follows:

~~~ c
#if !defined(_TP_H) || defined(TRACEPOINT_HEADER_MULTI_READ)
#define _TP_H
~~~

Add these precompiler conditionals to ensure the tracepoint event
generation can include this file more than once.

The `TRACEPOINT_EVENT()` macro is defined in a LTTng-UST header file which
must be included:

~~~ c
#include <lttng/tracepoint.h>
~~~

This also allows the application to use the `tracepoint()` macro.

Next is a list of `TRACEPOINT_EVENT()` macro calls which create the
actual tracepoint definitions. We skip this for the moment and
come back to how to use `TRACEPOINT_EVENT()`
[in a later section](#doc-defining-tracepoints). Just pay attention to
the first argument: it's always the name of the tracepoint provider
being defined in this header file.

End of include guard:

~~~ c
#endif /* _TP_H */
~~~

Finally, include `<lttng/tracepoint-event.h>` to expand the macros:

~~~ c
#include <lttng/tracepoint-event.h>
~~~

That's it for `tp.h`. Of course, this is only a header file; it must be
included in some C source file to actually use it. This is the job of
`tp.c`:

~~~ c
#define TRACEPOINT_CREATE_PROBES

#include "tp.h"
~~~

When `TRACEPOINT_CREATE_PROBES` is defined, the macros used in `tp.h`,
which is included just after, actually create the source code for
LTTng-UST probes (global data structures and functions) out of your
tracepoint definitions. How exactly this is done is out of this text's scope.
`TRACEPOINT_CREATE_PROBES` is discussed further
in [Building/linking tracepoint providers and the user application](#doc-building-tracepoint-providers-and-user-application).

You could include other header files like `tp.h` here to create the probes
of different tracepoint providers, e.g.:

~~~ c
#define TRACEPOINT_CREATE_PROBES

#include "tp1.h"
#include "tp2.h"
~~~

The rule is: probes of a given tracepoint provider
must be created in exactly one source file. This source file could be one
of your project's; it doesn't have to be on its own like `tp.c`, although
[a later section](#doc-building-tracepoint-providers-and-user-application)
shows that doing so allows packaging the tracepoint providers
independently and keep them out of your application, also making it
possible to reuse them between projects.

The following sections explain how to define tracepoints, how to use the
`tracepoint()` macro to instrument your user space C application and how
to build/link tracepoint providers and your application with LTTng-UST
support.
