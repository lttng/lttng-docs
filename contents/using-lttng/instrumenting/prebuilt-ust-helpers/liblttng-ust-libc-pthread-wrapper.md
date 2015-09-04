---
id: liblttng‑ust‑libc‑pthread-wrapper
since: 2.3
---

`liblttng-ust-libc-wrapper.so` and `liblttng-ust-pthread-wrapper.so`
can add instrumentation to respectively some C standard library and
POSIX threads functions.

The following functions are traceable by `liblttng-ust-libc-wrapper.so`:

<div class="table">
<table class="func-desc">
    <thead>
        <tr>
            <th><abbr title="Tracepoint">TP</abbr> provider name</th>
            <th><abbr title="Tracepoint">TP</abbr> name</th>
            <th>Instrumented function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="6">
                <code class="no-bg">ust_libc</code>
            </td>
            <td>
                <code class="no-bg">malloc</code>
            </td>
            <td>
                <code class="no-bg">malloc()</code>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">calloc</code>
            </td>
            <td>
                <code class="no-bg">calloc()</code>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">realloc</code>
            </td>
            <td>
                <code class="no-bg">realloc()</code>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">free</code>
            </td>
            <td>
                <code class="no-bg">free()</code>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">memalign</code>
            </td>
            <td>
                <code class="no-bg">memalign()</code>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">posix_memalign</code>
            </td>
            <td>
                <code class="no-bg">posix_memalign()</code>
            </td>
        </tr>
    </tbody>
</table>
</div>

The following functions are traceable by
`liblttng-ust-pthread-wrapper.so`:

<div class="table">
<table class="func-desc">
    <thead>
        <tr>
            <th><abbr title="Tracepoint">TP</abbr> provider name</th>
            <th><abbr title="Tracepoint">TP</abbr> name</th>
            <th>Instrumented function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="4">
                <code class="no-bg">ust_pthread</code>
            </td>
            <td>
                <code class="no-bg">pthread_mutex_lock_req</code>
            </td>
            <td>
                <code class="no-bg">pthread_mutex_lock()</code> (request time)
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">pthread_mutex_lock_acq</code>
            </td>
            <td>
                <code class="no-bg">pthread_mutex_lock()</code> (acquire time)
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">pthread_mutex_trylock</code>
            </td>
            <td>
                <code class="no-bg">pthread_mutex_trylock()</code>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">pthread_mutex_unlock</code>
            </td>
            <td>
                <code class="no-bg">pthread_mutex_unlock()</code>
            </td>
        </tr>
    </tbody>
</table>
</div>

All tracepoints have fields corresponding to the arguments of the
function they instrument.

To use one or the other with any user application, independently of
how the latter is built, do:

<pre class="term">
LD_PRELOAD=liblttng-ust-libc-wrapper.so my-app
</pre>

or

<pre class="term">
LD_PRELOAD=liblttng-ust-pthread-wrapper.so my-app
</pre>

To use both, do:

<pre class="term">
LD_PRELOAD="liblttng-ust-libc-wrapper.so liblttng-ust-pthread-wrapper.so" my-app
</pre>

When the shared object is preloaded, it effectively replaces the
functions listed in the above tables by wrappers which add tracepoints
and call the replaced functions.

Of course, like any other tracepoint, the ones above need to be enabled
in order for LTTng-UST to generate events. This is done using the
`lttng` command line tool
(see [Controlling tracing](#doc-controlling-tracing)).
