---
id: tracing-your-own-user-application
---

The previous section helped you create a trace out of Linux kernel events.
This section steps you through a simple example showing you how to trace
a _Hello world_ program written in C.

Make sure the LTTng-tools and LTTng-UST packages
[are installed](#doc-installing-lttng).

Tracing is just like having `printf()` calls at specific locations of
your source code, albeit LTTng is much faster and more flexible than
`printf()`. In the LTTng realm, **`tracepoint()`** is analogous to
`printf()`.

Unlike `printf()`, though, `tracepoint()` does not use a format string to
know the types of its arguments: the formats of all tracepoints must be
defined before using them. So before even writing our _Hello world_ program,
we need to define the format of our tracepoint. This is done by creating a
**tracepoint provider**, which consists of a tracepoint provider header
(`.h` file) and a tracepoint provider definition (`.c` file).

The tracepoint provider header contains some boilerplate as well as a
list of tracepoint definitions and other optional definition entries
which we skip for this quickstart. Each tracepoint is defined using the
`TRACEPOINT_EVENT()` macro. For each tracepoint, you must provide:

  * a **provider name**, which is the "scope" or namespace of this
    tracepoint (this usually includes the company and project names)
  * a **tracepoint name**
  * a **list of arguments** for the eventual `tracepoint()` call, each
    item being:
    * the argument C type
    * the argument name
  * a **list of fields**, which correspond to the actual fields of the
    recorded events for this tracepoint

Here's an example of a simple tracepoint provider header with two
arguments: an integer and a string:

~~~ c
#undef TRACEPOINT_PROVIDER
#define TRACEPOINT_PROVIDER hello_world

#undef TRACEPOINT_INCLUDE
#define TRACEPOINT_INCLUDE "./hello-tp.h"

#if !defined(_HELLO_TP_H) || defined(TRACEPOINT_HEADER_MULTI_READ)
#define _HELLO_TP_H

#include <lttng/tracepoint.h>

TRACEPOINT_EVENT(
    hello_world,
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

#endif /* _HELLO_TP_H */

#include <lttng/tracepoint-event.h>
~~~

The exact syntax is well explained in the
[C application](#doc-c-application) instrumentation guide of the
[Using LTTng](#doc-using-lttng) chapter, as well as in the
<a href="/man/3/lttng-ust" class="ext">LTTng-UST man page</a>.

Save the above snippet as `hello-tp.h`.

Write the tracepoint provider definition as `hello-tp.c`:

~~~ c
#define TRACEPOINT_CREATE_PROBES
#define TRACEPOINT_DEFINE

#include "hello-tp.h"
~~~

Create the tracepoint provider:

<pre class="term">
gcc -c -I. hello-tp.c
</pre>

Now, by including `hello-tp.h` in your own application, you may use the
tracepoint defined above by properly refering to it when calling
`tracepoint()`:

~~~ c
#include <stdio.h>
#include "hello-tp.h"

int main(int argc, char *argv[])
{
    int x;

    puts("Hello, World!\nPress Enter to continue...");

    /*
     * The following getchar() call is only placed here for the purpose
     * of this demonstration, for pausing the application in order for
     * you to have time to list its events. It's not needed otherwise.
     */
    getchar();

    /*
     * A tracepoint() call. Arguments, as defined in hello-tp.h:
     *
     *     1st: provider name (always)
     *     2nd: tracepoint name (always)
     *     3rd: my_integer_arg (first user-defined argument)
     *     4th: my_string_arg (second user-defined argument)
     *
     * Notice the provider and tracepoint names are NOT strings;
     * they are in fact parts of variables created by macros in
     * hello-tp.h.
     */
    tracepoint(hello_world, my_first_tracepoint, 23, "hi there!");

    for (x = 0; x < argc; ++x) {
        tracepoint(hello_world, my_first_tracepoint, x, argv[x]);
    }

    puts("Quitting now!");

    tracepoint(hello_world, my_first_tracepoint, x * x, "x^2");

    return 0;
}
~~~

Save this as `hello.c`, next to `hello-tp.c`.

Notice `hello-tp.h`, the tracepoint provider header, is included
by `hello.c`.

You are now ready to compile the application with LTTng-UST support:

<pre class="term">
gcc -c hello.c
gcc -o hello hello.o hello-tp.o -llttng-ust -ldl</strong>
</pre>

Here's the whole build process:

<figure class="img img-100">
<img src="/images/docs26/ust-flow.png" alt="User space tracing's build process">
<figcaption>
    User space tracing build process
</figcaption>
</figure>

If you followed the
[Tracing the Linux kernel](#doc-tracing-the-linux-kernel) tutorial, the
following steps should look familiar.

First, run the application with a few arguments:

<pre class="term">
./hello world and beyond
</pre>

You should see

~~~ text
Hello, World!
Press Enter to continue...
~~~

Use the `lttng` tool to list all available user space events:

<pre class="term">
lttng list --userspace
</pre>

You should see the `hello_world:my_first_tracepoint` tracepoint listed
under the `./hello` process.

Create a tracing session:

<pre class="term">
lttng create
</pre>

Enable the `hello_world:my_first_tracepoint` tracepoint:

<pre class="term">
lttng enable-event --userspace hello_world:my_first_tracepoint
</pre>

Start tracing:

<pre class="term">
lttng start
</pre>

Go back to the running `hello` application and press Enter. All `tracepoint()`
calls are executed and the program finally exits.

Stop tracing:

<pre class="term">
lttng stop
</pre>

Done! You may use `lttng view` to list the recorded events. This command
starts
<a href="http://diamon.org/babeltrace" class="ext"><code>babeltrace</code></a>
in the background, if it's installed:

<pre class="term">
lttng view
</pre>

should output something like:

~~~ text
[18:10:27.684304496] (+?.?????????) hostname hello_world:my_first_tracepoint: { cpu_id = 0 }, { my_string_field = "hi there!", my_integer_field = 23 }
[18:10:27.684338440] (+0.000033944) hostname hello_world:my_first_tracepoint: { cpu_id = 0 }, { my_string_field = "./hello", my_integer_field = 0 }
[18:10:27.684340692] (+0.000002252) hostname hello_world:my_first_tracepoint: { cpu_id = 0 }, { my_string_field = "world", my_integer_field = 1 }
[18:10:27.684342616] (+0.000001924) hostname hello_world:my_first_tracepoint: { cpu_id = 0 }, { my_string_field = "and", my_integer_field = 2 }
[18:10:27.684343518] (+0.000000902) hostname hello_world:my_first_tracepoint: { cpu_id = 0 }, { my_string_field = "beyond", my_integer_field = 3 }
[18:10:27.684357978] (+0.000014460) hostname hello_world:my_first_tracepoint: { cpu_id = 0 }, { my_string_field = "x^2", my_integer_field = 16 }
~~~

When you're done, you may destroy the tracing session, which does _not_
destroy the generated trace files, leaving them available for further
analysis:

<pre class="term">
lttng destroy
</pre>

The next section presents other alternatives to view and analyze your
LTTng traces.
