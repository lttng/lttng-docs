---
id: static-linking
---

With the static linking method, compiled tracepoint providers are copied
into the target application. There are three ways to do this:

  1. Use one of your **existing C source files** to create probes.
  2. Create probes in a separate C source file and build it as an
     **object file** to be linked with the application (more decoupled).
  3. Create probes in a separate C source file, build it as an
     object file and archive it to create a **static library**
     (more decoupled, more portable).

The first approach is to define `TRACEPOINT_CREATE_PROBES` and include
your tracepoint provider(s) header file(s) directly into an existing C
source file. Here's an example:

~~~ c
#include <stdlib.h>
#include <stdio.h>
/* ... */

#define TRACEPOINT_CREATE_PROBES
#define TRACEPOINT_DEFINE
#include "tp.h"

/* ... */

int my_func(int a, const char* b)
{
    /* ... */

    tracepoint(my_provider, my_tracepoint, buf, sz, limit, &tt)

    /* ... */
}

/* ... */
~~~

Again, before including a given tracepoint provider header file,
`TRACEPOINT_CREATE_PROBES` and `TRACEPOINT_DEFINE` must be defined in
one, **and only one**, translation unit. Other C source files of the
same application may include `tp.h` to use tracepoints with
the `tracepoint()` macro, but must not define
`TRACEPOINT_CREATE_PROBES`/`TRACEPOINT_DEFINE` again.

This translation unit may be built as an object file by making sure to
add `.` to the include path:

<pre class="term">
gcc -c <strong>-I.</strong> file.c
</pre>

The second approach is to isolate the tracepoint provider code into a
separate object file by using a dedicated C source file to create probes:

~~~ c
#define TRACEPOINT_CREATE_PROBES

#include "tp.h"
~~~

`TRACEPOINT_DEFINE` must be defined by a translation unit of the
application. Since we're talking about static linking here, it could as
well be defined directly in the file above, before `#include "tp.h"`:

~~~ c
#define TRACEPOINT_CREATE_PROBES
#define TRACEPOINT_DEFINE

#include "tp.h"
~~~

This is actually what [`lttng-gen-tp`](#doc-lttng-gen-tp) does, and is
the recommended practice.

Build the tracepoint provider:

<pre class="term">
gcc -c -I. tp.c
</pre>

Finally, the resulting object file may be archived to create a
more portable tracepoint provider static library:

<pre class="term">
ar rc tp.a tp.o
</pre>

Using a static library does have the advantage of centralising the
tracepoint providers objects so they can be shared between multiple
applications. This way, when the tracepoint provider is modified, the
source code changes don't have to be patched into each application's source
code tree. The applications need to be relinked after each change, but need
not to be otherwise recompiled (unless the tracepoint provider's API
changes).

Regardless of which method you choose, you end up with an object file
(potentially archived) containing the trace providers assembled code.
To link this code with the rest of your application, you must also link
with `liblttng-ust` and `libdl`:

<pre class="term">
gcc -o app <strong>tp.o</strong> other.o files.o of.o your.o app.o <strong>-llttng-ust -ldl</strong>
</pre>

or

<pre class="term">
gcc -o app <strong>tp.a</strong> other.o files.o of.o your.o app.o -llttng-ust -ldl
</pre>

If you're using a <abbr title="Berkeley Software Distribution">BSD</abbr>
system, replace `-ldl` with `-lc`:

<pre class="term">
gcc -o app tp.a other.o files.o of.o your.o app.o -llttng-ust <strong>-lc</strong>
</pre>

The application can be started as usual, for example:

<pre class="term">
./app
</pre>

The `lttng` command line tool can be used to
[control tracing](#doc-controlling-tracing).
