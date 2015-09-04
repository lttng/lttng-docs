---
id: liblttng‑ust‑dl
since: 2.4
---

This LTTng-UST helper causes all calls to `dlopen()` and `dlclose()`
in the target application to be traced with LTTng.

The helper's shared object, `liblttng-ust-dl.so`, registers the
following tracepoints when preloaded:

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
                <code class="no-bg">ust_baddr</code>
            </td>
            <td>
                <code class="no-bg">push</code>
            </td>
            <td>
                <p><code>dlopen()</code> call</p>

                <ul>
                    <li>
                        <code class="arg">baddr</code>&nbsp;memory
                        base address
                        (where the dynamic linker placed the shared
                        object)
                    </li>
                    <li>
                        <code class="arg">sopath</code>&nbsp;file system
                        path to the loaded shared object
                    </li>
                    <li>
                        <code class="arg">size</code>&nbsp;file size
                        of the the loaded shared object
                    </li>
                    <li>
                        <code class="arg">mtime</code>&nbsp;last
                        modification time (seconds since Epoch time)
                        of the loaded shared object
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <code class="no-bg">pop</code>
            </td>
            <td>
                <p><code>dlclose()</code> call</p>

                <ul>
                    <li>
                        <code class="arg">baddr</code>&nbsp;memory
                        base address
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

To use this LTTng-UST helper with any user application, independently of
how the latter is built, do:

<pre class="term">
LD_PRELOAD=liblttng-ust-dl.so my-app
</pre>

Of course, like any other tracepoint, the ones above need to be enabled
in order for LTTng-UST to generate events. This is done using the
`lttng` command line tool
(see [Controlling tracing](#doc-controlling-tracing)).
