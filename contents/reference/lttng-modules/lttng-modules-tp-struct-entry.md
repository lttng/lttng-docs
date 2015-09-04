---
id: lttng-modules-tp-struct-entry
---

This table describes possible entries for the `TP_STRUCT__entry()` part
of `LTTNG_TRACEPOINT_EVENT()`:

<div class="table">
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
                    <li><code class="no-bg">__field(<span class="arg">t</span>, <span class="arg">n</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Standard integer, displayed in base&nbsp;10</p>
                <ul>
                    <li>
                        <code class="arg">t</code> integer C type
                        (<code>int</code>, <code>unsigned char</code>,
                        <code>size_t</code>, ...)
                    </li>
                    <li><code class="arg">n</code> field name</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__field_hex(<span class="arg">t</span>, <span class="arg">n</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Standard integer, displayed in base&nbsp;16</p>
                <ul>
                    <li><code class="arg">t</code> integer C type</li>
                    <li><code class="arg">n</code> field name</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__field_oct(<span class="arg">t</span>, <span class="arg">n</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Standard integer, displayed in base&nbsp;8</p>
                <ul>
                    <li>
                        <code class="arg">t</code> integer C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__field_network(<span class="arg">t</span>, <span class="arg">n</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Integer in network byte order (big endian),
                    displayed in base&nbsp;10
                </p>
                <ul>
                    <li>
                        <code class="arg">t</code> integer C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__field_network_hex(<span class="arg">t</span>, <span class="arg">n</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Integer in network byte order (big endian),
                    displayed in base&nbsp;16
                </p>
                <ul>
                    <li>
                        <code class="arg">t</code> integer C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__array(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Statically-sized array, elements displayed in base&nbsp;10</p>
                <ul>
                    <li>
                        <code class="arg">t</code> array element C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> number of elements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__array_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Statically-sized array, elements displayed in base&nbsp;16</p>
                <ul>
                    <li>
                        <code class="arg">t</code> array element C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> number of elements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__array_text(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Statically-sized array, displayed as text</p>
                <ul>
                    <li>
                        <code class="arg">t</code> array element C type
                        (always <code>char</code>)
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> number of elements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__dynamic_array(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Dynamically-sized array, displayed in base&nbsp;10</p>
                <ul>
                    <li>
                        <code class="arg">t</code> array element C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> length C expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__dynamic_array_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Dynamically-sized array, displayed in base&nbsp;16</p>
                <ul>
                    <li>
                        <code class="arg">t</code> array element C type
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> length C expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__dynamic_array_text(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Dynamically-sized array, displayed as text</p>
                <ul>
                    <li>
                        <code class="arg">t</code> array element C type
                        (always <code>char</code>)
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> length C expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">__string(<span class="arg">n</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Null-terminated string; undefined behavior
                    if <code class="arg">s</code> is <code>NULL</code>
                </p>
                <ul>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">s</code> string source (pointer)</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

The above macros should cover the majority of cases. For advanced items,
see `probes/lttng-events.h`.
