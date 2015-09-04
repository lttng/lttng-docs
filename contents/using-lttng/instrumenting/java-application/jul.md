---
id: jul
---

Here's an example of tracing a Java application which is using
**`java.util.logging`**:

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

The LTTng-UST Java agent is packaged in a JAR file named
`liblttng-ust-agent.jar` It is typically located in
`/usr/lib/lttng/java`. To compile the snippet above
(saved as `Test.java`), do:

<pre class="term">
javac -cp /usr/lib/lttng/java/liblttng-ust-agent.jar Test.java
</pre>

You can run the resulting compiled class like this:

<pre class="term">
java -cp /usr/lib/lttng/java/liblttng-ust-agent.jar:. Test
</pre>

<div class="tip">
<p>
    <span class="t">Note:</span><a href="http://openjdk.java.net/" class="ext">OpenJDK</a> 7
    is used for development and continuous integration, thus this
    version is directly supported. However, the LTTng-UST Java agent has
    also been tested with OpenJDK 6.
</p>
</div>
