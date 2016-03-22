---
id: lttng-modules-tp-fields
since: 2.7
---

<a name="doc-lttng-modules-tp-fast-assign"></a>
<a name="doc-lttng-modules-tp-struct-entry"></a>
The available macros to define tracepoint fields, which should be listed
within `TP_FIELDS()` in `LTTNG_TRACEPOINT_EVENT()`, are:

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
                    <li><code class="no-bg">ctf_integer(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_integer_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_integer(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_integer_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Standard integer, displayed in base&nbsp;10</p>
                <ul>
                    <li>
                        <code class="arg"><strong>t</strong></code> integer C type
                        (<code>int</code>, <code>long</code>,
                        <code>size_t</code>, ...)
                    </li>
                    <li><code class="arg"><strong>n</strong></code> field name</li>
                    <li><code class="arg"><strong>e</strong></code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_integer_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_integer_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Standard integer, displayed in base&nbsp;16</p>
                <ul>
                    <li><code class="arg"><strong>t</strong></code> integer C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><code class="no-bg">ctf_integer_oct(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></td>
            <td>
                <p>Standard integer, displayed in base&nbsp;8</p>
                <ul>
                    <li><code class="arg"><strong>t</strong></code> integer C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_integer_network(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_integer_network(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Integer in network byte order (big-endian),
                    displayed in base&nbsp;10
                </p>
                <ul>
                    <li><code class="arg">t</code> integer C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_integer_network_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_integer_network_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Integer in network byte order, displayed
                    in base&nbsp;16</p>
                <ul>
                    <li><code class="arg">t</code> integer C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_float(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_float(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_float_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_float_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>Floating point number</p>
                <ul>
                    <li>
                        <code class="arg">t</code> floating point number
                        C type (<code>float</code>, <code>double</code>)
                    </li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_string(<span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_string(<span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_string_nowrite(<span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                    <li><code class="no-bg">ctf_user_string_nowrite(<span class="arg">n</span>, <span class="arg">e</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Null-terminated string; undefined behavior if
                    <code class="arg">e</code> is <code>NULL</code>
                </p>
                <ul>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_array(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                    <li><code class="no-bg">ctf_user_array(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                    <li><code class="no-bg">ctf_array_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                    <li><code class="no-bg">ctf_user_array_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Statically-sized array of integers, displayed in
                    base&nbsp;10
                </p>
                <ul>
                    <li><code class="arg">t</code> array element C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                    <li><code class="arg">s</code> number of elements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_array_text(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                    <li><code class="no-bg">ctf_user_array_text(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                    <li><code class="no-bg">ctf_array_text_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                    <li><code class="no-bg">ctf_user_array_text_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">s</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Statically-sized array, printed as text; no need to
                    be null-terminated
                </p>
                <ul>
                    <li><code class="arg">t</code> array element C type (always <code>char</code>)</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                    <li><code class="arg">s</code> number of elements</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_sequence(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                    <li><code class="no-bg">ctf_user_sequence(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                    <li><code class="no-bg">ctf_sequence_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                    <li><code class="no-bg">ctf_user_sequence_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Dynamically-sized array of integers, displayed in
                    base&nbsp;10; type of
                    <code class="arg">E</code> needs to be unsigned
                </p>
                <ul>
                    <li><code class="arg">t</code> sequence element C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                    <li><code class="arg">T</code> length expression C type</li>
                    <li><code class="arg">E</code> length expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_sequence_hex(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Dynamically-sized array of integers, displayed in
                    base&nbsp;16; type of
                    <code class="arg">E</code> needs to be unsigned
                </p>
                <ul>
                    <li><code class="arg">t</code> sequence element C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                    <li><code class="arg">T</code> length expression C type</li>
                    <li><code class="arg">E</code> length expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_sequence_network(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Dynamically-sized array of integers in network byte
                    order (big endian), displayed in base&nbsp;10;
                    type of



                    <code class="arg">E</code> needs to be unsigned
                </p>
                <ul>
                    <li><code class="arg">t</code> sequence element C type</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                    <li><code class="arg">T</code> length expression C type</li>
                    <li><code class="arg">E</code> length expression</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><code class="no-bg">ctf_sequence_text(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                    <li><code class="no-bg">ctf_user_sequence_text(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                    <li><code class="no-bg">ctf_sequence_text_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                    <li><code class="no-bg">ctf_user_sequence_text_nowrite(<span class="arg">t</span>, <span class="arg">n</span>, <span class="arg">e</span>, <span class="arg">T</span>, <span class="arg">E</span>)</code></li>
                </ul>
            </td>
            <td>
                <p>
                    Dynamically-sized array, displayed as text; no need to
                    be null-terminated; undefined behavior if
                    <code class="arg">e</code> is <code>NULL</code></p>
                <ul>
                    <li><code class="arg">t</code> sequence element C type (always <code>char</code>)</li>
                    <li><code class="arg">n</code> field name</li>
                    <li><code class="arg">e</code> argument expression</li>
                    <li><code class="arg">T</code> length expression C type</li>
                    <li><code class="arg">E</code> length expression</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

The `_user` versions must be used when the argument expression, `e`, is
a user space address. In the cases of `ctf_user_integer*()` and
`ctf_user_float*()`, `&e` must be a user space address, thus `e` must
be addressable.

The `_nowrite` versions omit themselves from the session trace, but are
otherwise identical. This means the `_nowrite` fields won't be written
in the recorded trace. Their primary purpose is to make some
of the event context available to the
[event filters](#doc-enabling-disabling-events) without having to
commit the data to sub-buffers.
