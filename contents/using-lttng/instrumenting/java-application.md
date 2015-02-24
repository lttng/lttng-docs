---
id: java-application
---

LTTng-UST provides a _logging_ back-end for Java applications using
either
<a href="http://docs.oracle.com/javase/7/docs/api/java/util/logging/Logger.html" class="ext"><code>java.util.logging</code></a>
(JUL), or
<a href="http://logging.apache.org/log4j/1.2/" class="ext">Apache log4j 1.2</a>.
This back-end is called the _LTTng-UST Java agent_, and is responsible
for communications with an LTTng session daemon.

<div class="tip">
<p>
    <span class="t">Note:</span>The latest stable version of LTTng
    does not support Log4j 2.
</p>
</div>

From the user's point of view, once the LTTng-UST Java agent has been
initialized, JUL and log4j loggers may be created and used as usual.
The agent adds its own handler to the _root logger_, so that all
loggers may generate LTTng events with no effort.

Common JUL/log4j features are supported using the `lttng` tool
(see [Controlling tracing](#doc-controlling-tracing)):

  * listing all logger names
  * enabling/disabling events per logger name
  * JUL/log4j log levels

Here's an example using **`java.util.logging`**:

~~~ java
import java.util.logging.Logger;
import org.lttng.ust.agent.LTTngAgent;

public class Test
{
    private static final int answer = 42;

    public static void main(String[] argv) throws Exception
    {
        // create a logger
        Logger logger = Logger.getLogger("jello");

        // call this as soon as possible (before logging)
        LTTngAgent lttngAgent = LTTngAgent.getLTTngAgent();

        // log at will!
        logger.info("some info");
        logger.warning("some warning");
        Thread.sleep(500);
        logger.finer("finer information; the answer is " + answer);
        Thread.sleep(123);
        logger.severe("error!");

        // not mandatory, but cleaner
        lttngAgent.dispose();
    }
}
~~~

Here's the same example, this time using **log4j**:

~~~ java
import org.apache.log4j.Logger;
import org.apache.log4j.BasicConfigurator;
import org.lttng.ust.agent.LTTngAgent;

public class Test
{
    private static final int answer = 42;

    public static void main(String[] argv) throws Exception
    {
        // create and configure a logger
        Logger logger = Logger.getLogger(Test.class);
        BasicConfigurator.configure();

        // call this as soon as possible (before logging)
        LTTngAgent lttngAgent = LTTngAgent.getLTTngAgent();

        // log at will!
        logger.info("some info");
        logger.warn("some warning");
        Thread.sleep(500);
        logger.debug("debug information; the answer is " + answer);
        Thread.sleep(123);
        logger.error("error!");
        logger.fatal("fatal error!");

        // not mandatory, but cleaner
        lttngAgent.dispose();
    }
}
~~~

The LTTng-UST Java agent classes are packaged in a JAR file named
`liblttng-ust-agent.jar`. It is typically located in
`/usr/lib/lttng/java`. To compile the snippets above
(saved as `Test.java`), do:

<pre class="term">
javac -cp /usr/lib/lttng/java/liblttng-ust-agent.jar:$LOG4JCP Test.java
</pre>

where `$LOG4JCP` is the log4j 1.2 JAR file path, if you're using log4j.

You can run the resulting compiled class like this:

<pre class="term">
java -cp /usr/lib/lttng/java/liblttng-ust-agent.jar:$LOG4JCP:. Test
</pre>

<div class="tip">
<p>
    <span class="t">Note:</span><a href="http://openjdk.java.net/" class="ext">OpenJDK</a> 7
    is used for development and continuous integration, thus this
    version is directly supported. However, the LTTng-UST Java agent has
    also been tested with OpenJDK 6.
</p>
</div>
