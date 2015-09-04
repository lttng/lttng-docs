---
id: viewing-and-analyzing-your-traces
---

This section describes how to visualize the data gathered after tracing
the Linux kernel or a user space application.

Many ways exist to read your LTTng traces:

  * **`babeltrace`** is a command line utility which converts trace formats;
    it supports the format used by LTTng,
    <abbr title="Common Trace Format">CTF</abbr>, as well as a basic
    text output which may be `grep`ed. The `babeltrace` command is
    part of the
    <a href="http://www.efficios.com/babeltrace" class="ext">Babeltrace</a> project.
  * Babeltrace also includes a **Python binding** so that you may
    easily open and read an LTTng trace with your own script, benefiting
    from the power of Python.
  * **<a href="http://projects.eclipse.org/projects/tools.tracecompass" class="ext">Trace Compass</a>**
    is an Eclipse plugin used to visualize and analyze various types of
    traces, including LTTng's. It also comes as a standalone application
    and can be downloaded from
    <a href="http://projects.eclipse.org/projects/tools.tracecompass/downloads" class="ext">here</a>.

LTTng trace files are usually recorded in the `~/lttng-traces` directory.
Let's now view the trace and perform a basic analysis using
`babeltrace`.

The simplest way to list all the recorded events of a trace is to pass its
path to `babeltrace` with no options:

<pre class="term">
babeltrace ~/lttng-traces/my-session
</pre>

`babeltrace` finds all traces within the given path recursively and
prints all their events, merging them in order of time.

Listing all the system calls of a Linux kernel trace with their arguments is
easy with `babeltrace` and `grep`:

<pre class="term">
babeltrace ~/lttng-traces/my-kernel-session | grep sys_
</pre>

Counting events is also straightforward:

<pre class="term">
babeltrace ~/lttng-traces/my-kernel-session | grep sys_read | wc --lines
</pre>

The text output of `babeltrace` is useful for isolating events by simple
matching using `grep` and similar utilities. However, more elaborate filters
such as keeping only events with a field value falling within a specific range
are not trivial to write using a shell. Moreover, reductions and even the
most basic computations involving multiple events are virtually impossible
to implement.

Fortunately, Babeltrace ships with a Python 3 binding which makes it
really easy to read the events of an LTTng trace sequentially and compute
the desired information.

Here's a simple example using the Babeltrace Python binding. The following
script accepts an LTTng Linux kernel trace path as its first argument and
outputs the short names of the top 5 running processes on CPU 0 during the
whole trace:

~~~ python
import sys
from collections import Counter
import babeltrace


def top5proc():
    if len(sys.argv) != 2:
        msg = 'Usage: python {} TRACEPATH'.format(sys.argv[0])
        raise ValueError(msg)

    # a trace collection holds one to many traces
    col = babeltrace.TraceCollection()

    # add the trace provided by the user
    # (LTTng traces always have the 'ctf' format)
    if col.add_trace(sys.argv[1], 'ctf') is None:
        raise RuntimeError('Cannot add trace')

    # this counter dict will hold execution times:
    #
    #   task command name -> total execution time (ns)
    exec_times = Counter()

    # this holds the last `sched_switch` timestamp
    last_ts = None

    # iterate events
    for event in col.events:
        # keep only `sched_switch` events
        if event.name != 'sched_switch':
            continue

        # keep only events which happened on CPU 0
        if event['cpu_id'] != 0:
            continue

        # event timestamp
        cur_ts = event.timestamp

        if last_ts is None:
            # we start here
            last_ts = cur_ts

        # previous task command (short) name
        prev_comm = event['prev_comm']

        # initialize entry in our dict if not yet done
        if prev_comm not in exec_times:
            exec_times[prev_comm] = 0

        # compute previous command execution time
        diff = cur_ts - last_ts

        # update execution time of this command
        exec_times[prev_comm] += diff

        # update last timestamp
        last_ts = cur_ts

    # display top 10
    for name, ns in exec_times.most_common(5):
        s = ns / 1000000000
        print('{:20}{} s'.format(name, s))


if __name__ == '__main__':
    top5proc()
~~~

Save this script as `top5proc.py` and run it with Python 3, providing the
path to an LTTng Linux kernel trace as the first argument:

<pre class="term">
python3 top5proc.py ~/lttng-sessions/my-session-.../kernel
</pre>

Make sure the path you provide is the directory containing actual trace
files (`channel0_0`, `metadata`, and the rest): the `babeltrace` utility
recurses directories, but the Python binding does not.

Here's an example of output:

~~~ text
swapper/0           48.607245889 s
chromium            7.192738188 s
pavucontrol         0.709894415 s
Compositor          0.660867933 s
Xorg.bin            0.616753786 s
~~~

Note that `swapper/0` is the "idle" process of CPU 0 on Linux; since we
weren't using the CPU that much when tracing, its first position in the list
makes sense.
