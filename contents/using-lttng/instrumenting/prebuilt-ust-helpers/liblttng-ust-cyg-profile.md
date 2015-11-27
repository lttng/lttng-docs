---
id: liblttng-ust-cyg-profile
---

Function tracing is the recording of which functions are entered and
left during the execution of an application. Like with any LTTng event,
the precise time at which this happens is also kept.

GCC and clang have an option named
<a href="https://gcc.gnu.org/onlinedocs/gcc-4.9.1/gcc/Code-Gen-Options.html" class="ext"><code>-finstrument-functions</code></a>
which generates instrumentation calls for entry and exit to functions.
The LTTng-UST function tracing helpers, `liblttng-ust-cyg-profile.so`
and `liblttng-ust-cyg-profile-fast.so`, take advantage of this feature
to add instrumentation to the two generated functions (which contain
`cyg_profile` in their names, hence the shared object's name).

In order to use LTTng-UST function tracing, the translation units to
instrument must be built using the `-finstrument-functions` compiler
flag.

LTTng-UST function tracing comes in two flavors, each providing
different trade-offs: `liblttng-ust-cyg-profile-fast.so` and
`liblttng-ust-cyg-profile.so`.

**`liblttng-ust-cyg-profile-fast.so`** is a lightweight variant that
should only be used where it can be _guaranteed_ that the complete event
stream is recorded without any missing events. Any kind of duplicate
information is left out. This version registers the following
tracepoints:

<div class="table">
<table class="func-desc">
    <thead>
        <tr>
            <th><abbr title="Tracepoint">TP</abbr> provider name</th>
            <th><abbr title="Tracepoint">TP</abbr> name</th>
            <th>Description/fields</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">
                <code class="no-bg">lttng_ust_cyg_profile_fast</code>
            </td>
            <td>
                <code class="no-bg">func_entry</code>
            </td>
            <td>
                <p>Function entry</p>

                <ul>
                    <li>
                        <code class="arg">addr</code>&nbsp;address of the
                        called function
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">func_exit</code>
            </td>
            <td>
                <p>Function exit</p>
            </td>
        </tr>
    </tbody>
</table>
</div>

Assuming no event is lost, having only the function addresses on entry
is enough for creating a call graph (remember that a recorded event
always contains the ID of the CPU that generated it). A tool like
<a href="https://sourceware.org/binutils/docs/binutils/addr2line.html" class="ext"><code>addr2line</code></a>
may be used to convert function addresses back to source files names
and line numbers.

The other helper,
**`liblttng-ust-cyg-profile.so`**,
is a more robust variant which also works for use cases where
events might get discarded or not recorded from application startup.
In these cases, the trace analyzer needs extra information to be
able to reconstruct the program flow. This version registers the
following tracepoints:

<div class="table">
<table class="func-desc">
    <thead>
        <tr>
            <th><abbr title="Tracepoint">TP</abbr> provider name</th>
            <th><abbr title="Tracepoint">TP</abbr> name</th>
            <th>Description/fields</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">
                <code class="no-bg">lttng_ust_cyg_profile</code>
            </td>
            <td>
                <code class="no-bg">func_entry</code>
            </td>
            <td>
                <p>Function entry</p>

                <ul>
                    <li>
                        <code class="arg">addr</code>&nbsp;address of the
                        called function
                    </li>
                    <li>
                        <code class="arg">call_site</code>&nbsp;call site
                        address
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">func_exit</code>
            </td>
            <td>
                <p>Function exit</p>

                <ul>
                    <li>
                        <code class="arg">addr</code>&nbsp;address of the
                        called function
                    </li>
                    <li>
                        <code class="arg">call_site</code>&nbsp;call site
                        address
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

To use one or the other variant with any user application, assuming at
least one translation unit of the latter is compiled with the
`-finstrument-functions` option, do:

<pre class="term">
LD_PRELOAD=liblttng-ust-cyg-profile-fast.so my-app
</pre>

or

<pre class="term">
LD_PRELOAD=liblttng-ust-cyg-profile.so my-app
</pre>

It might be necessary to limit the number of source files where
`-finstrument-functions` is used to prevent excessive amount of trace
data to be generated at runtime.

<div class="tip">
<p>
    <span class="t">Tip:</span> When using GCC, at least, you may use
    the
    <code>-finstrument-functions-exclude-function-list</code>
    option to avoid instrumenting entries and exits of specific
    symbol names.
</p>
</div>

All events generated from LTTng-UST function tracing are provided on
log level `TRACE_DEBUG_FUNCTION`, which is useful to easily enable
function tracing events in your tracing session using the
`--loglevel-only` option of `lttng enable-event`
(see [Controlling tracing](#doc-controlling-tracing)).
