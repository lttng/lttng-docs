---
id: java-application
---

LTTng-UST provides a _logging_ back-end for Java applications using
<a href="http://docs.oracle.com/javase/7/docs/api/java/util/logging/Logger.html" class="ext">Java Util Logging</a> (JUL). This back-end is called the _LTTng-UST JUL agent_ and is
responsible for communications with an LTTng session daemon.

From the user's point of view, once the LTTng-UST JUL agent has been
initialized, JUL loggers may be created and used as usual. The agent
adds its own handler to the _root logger_, so that all loggers may
generate LTTng events with no effort.

Common JUL features are supported using the `lttng` tool
(see [Controlling tracing](#doc-controlling-tracing)):

  * listing all logger names
  * enabling/disabling events per logger name
  * JUL log levels

Here's an example:

~~~ java
import java.util.logging.Logger;
import org.lttng.ust.jul.LTTngAgent;

public class Test
{
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
        logger.finer("finer information...");
        Thread.sleep(123);
        logger.severe("error!");

        // not mandatory, but cleaner
        lttngAgent.dispose();
    }
}
~~~

The LTTng-UST JUL agent Java classes are packaged in a JAR file named
`liblttng-ust-jul.jar`. It is typically located in
`/usr/lib/lttng/java`. To compile the snippet above
(saved as `Test.java`), do:

<pre class="term">
javac -cp /usr/lib/lttng/java/liblttng-ust-jul.jar Test.java
</pre>

You can run the resulting compiled class:

<pre class="term">
java -cp /usr/lib/lttng/java/liblttng-ust-jul.jar:. Test
</pre>

<div class="tip">
<p>
    <span class="t">Note:</span><a href="http://openjdk.java.net/" class="ext">OpenJDK</a> 7
    is used for development and continuous integration, thus this
    version is directly supported. However, the LTTng-UST JUL agent has
    also been tested with OpenJDK 6.
</p>
</div>
