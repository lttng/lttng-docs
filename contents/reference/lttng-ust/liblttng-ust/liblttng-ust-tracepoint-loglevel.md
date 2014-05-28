---
id: liblttng-ust-tracepoint-loglevel
---

The following table shows the available log level values for the
`TRACEPOINT_LOGLEVEL()` macro:

<table class="func-desc">
    <thead>
        <tr>
            <th>Enum label</th>
            <th>Enum value</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code class="no-bg">TRACE_EMERG</code></td>
            <td>0</td>
            <td>System is unusable</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_ALERT</code></td>
            <td>1</td>
            <td>Action must be taken immediately</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_CRIT</code></td>
            <td>2</td>
            <td>Critical conditions</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_ERR</code></td>
            <td>3</td>
            <td>Error conditions</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_WARNING</code></td>
            <td>4</td>
            <td>Warning conditions</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_NOTICE</code></td>
            <td>5</td>
            <td>Normal, but significant, condition</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_INFO</code></td>
            <td>6</td>
            <td>Informational message</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_SYSTEM</code></td>
            <td>7</td>
            <td>Debug information with system-level scope (set of programs)</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_PROGRAM</code></td>
            <td>8</td>
            <td>Debug information with program-level scope (set of processes)</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_PROCESS</code></td>
            <td>9</td>
            <td>Debug information with process-level scope (set of modules)</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_MODULE</code></td>
            <td>10</td>
            <td>Debug information with module (executable/library) scope (set of units)</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_UNIT</code></td>
            <td>11</td>
            <td>Debug information with compilation unit scope (set of functions)</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_FUNCTION</code></td>
            <td>12</td>
            <td>Debug information with function-level scope</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG_LINE</code></td>
            <td>13</td>
            <td>Debug information with line-level scope (<code>TRACEPOINT_EVENT</code> default)</td>
        </tr>
        <tr>
            <td><code class="no-bg">TRACE_DEBUG</code></td>
            <td>14</td>
            <td>Debug-level message</td>
        </tr>
    </tbody>
</table>

Higher log level numbers imply the most verbosity (expect higher tracing
throughput). Log levels 0 through 6 and log level 14 match
<a href="http://man7.org/linux/man-pages/man3/syslog.3.html" class="ext">syslog</a>
level semantics. Log levels 7 through 13 offer more fine-grained
selection of debug information.
