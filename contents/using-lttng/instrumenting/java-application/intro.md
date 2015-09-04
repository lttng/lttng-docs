---
id: java-application
since: 2.4
---

LTTng-UST provides a _logging_ back-end for Java applications using
either
<a href="http://docs.oracle.com/javase/7/docs/api/java/util/logging/Logger.html" class="ext"><code>java.util.logging</code></a>
(JUL) or
<a href="http://logging.apache.org/log4j/1.2/" class="ext">Apache log4j 1.2</a>.
This back-end is called the _LTTng-UST Java agent_, and it is responsible
for the communications with an LTTng session daemon.

From the user's point of view, once the LTTng-UST Java agent has been
initialized, JUL and log4j loggers may be created and used as usual.
The agent adds its own handler to the _root logger_, so that all
loggers may generate LTTng events with no effort.

Common JUL/log4j features are supported using the `lttng` tool
(see [Controlling tracing](#doc-controlling-tracing)):

  * listing all logger names
  * enabling/disabling events per logger name
  * JUL/log4j log levels
