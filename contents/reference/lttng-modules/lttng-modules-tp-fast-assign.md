---
id: lttng-modules-tp-fast-assign
---

This table describes possible entries for the `TP_fast_assign()` part
of `LTTNG_TRACEPOINT_EVENT()`:

<table class="func-desc">
    <thead>
        <tr>
            <th>Macro</th>
            <th>Description/arguments</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">tp_assign(<span class="arg">d</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Assignment of C expression <code class="arg">s</code>
                    to tracepoint field <code class="arg">d</code>
                </p>
                <ul>
                    <li>
                        <code class="arg">d</code> name of destination
                        tracepoint field
                    </li>
                    <li>
                        <code class="arg">s</code> source C expression
                        (may refer to tracepoint arguments)
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">tp_memcpy(<span class="arg">d</span>, <span class="arg">s</span>, <span class="arg">l</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Memory copy of <code class="arg">l</code> bytes from
                    <code class="arg">s</code> to tracepoint field
                    <code class="arg">d</code> (use with array fields)
                </p>
                <ul>
                    <li>
                        <code class="arg">d</code> name of destination
                        tracepoint field
                    </li>
                    <li>
                        <code class="arg">s</code> source C expression
                        (may refer to tracepoint arguments)
                    </li>
                    <li>
                        <code class="arg">l</code> number of bytes to
                        copy
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">tp_memcpy_from_user(<span class="arg">d</span>, <span class="arg">s</span>, <span class="arg">l</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Memory copy of <code class="arg">l</code> bytes from
                    user space <code class="arg">s</code> to tracepoint field
                    <code class="arg">d</code> (use with array fields)
                </p>
                <ul>
                    <li>
                        <code class="arg">d</code> name of destination
                        tracepoint field
                    </li>
                    <li>
                        <code class="arg">s</code> source C expression
                        (may refer to tracepoint arguments)
                    </li>
                    <li>
                        <code class="arg">l</code> number of bytes to
                        copy
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">tp_memcpy_dyn(<span class="arg">d</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Memory copy of dynamically-sized array
                    from <code class="arg">s</code> to tracepoint field
                    <code class="arg">d</code>; number of bytes is
                    known from the field's length expression (use with
                    dynamically-sized array fields)
                </p>
                <ul>
                    <li>
                        <code class="arg">d</code> name of destination
                        tracepoint field
                    </li>
                    <li>
                        <code class="arg">s</code> source C expression
                        (may refer to tracepoint arguments)
                    </li>
                    <li>
                        <code class="arg">l</code> number of bytes to
                        copy
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">tp_strcpy(<span class="arg">d</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    String copy of <code class="arg">s</code>
                    to tracepoint field <code class="arg">d</code>
                    (use with string fields)
                </p>
                <ul>
                    <li>
                        <code class="arg">d</code> name of destination
                        tracepoint field
                    </li>
                    <li>
                        <code class="arg">s</code> source C expression
                        (may refer to tracepoint arguments)
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
