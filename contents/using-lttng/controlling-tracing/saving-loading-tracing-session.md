---
id: saving-loading-tracing-session
---

Configuring a tracing session may be long: creating and enabling
channels with specific parameters, enabling kernel and user space
domain events with specific log levels and filters, adding context
to some channels, etc. If you're going to use LTTng to solve real
world problems, chances are you're going to have to record events using
the same tracing session setup over and over, modifying a few variables
each time in your instrumented program or environment. To avoid
constant tracing session reconfiguration, the `lttng` tool is able to
save and load tracing session configurations to/from XML files.

To save a given tracing session configuration, do:

<pre class="term">
lttng save my-session
</pre>

where `my-session` is the name of the tracing session to save. Tracing
session configurations are saved to `~/.lttng/sessions` by default;
use the `--output-path` option to change this destination directory.

All configuration parameters are saved:

  * tracing session name
  * trace data output path
  * channels with their state and all their parameters
  * context information added to channels
  * events with their state, log level and filter
  * tracing activity (started or stopped)

To load a tracing session, simply do:

<pre class="term">
lttng load my-session
</pre>

or, if you used a custom path:

<pre class="term">
lttng load --input-path /path/to/my-session.lttng
</pre>

Your saved tracing session is restored as if you just configured
it manually.
