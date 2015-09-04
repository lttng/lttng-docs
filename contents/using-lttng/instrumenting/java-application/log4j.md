---
id: log4j
since: 2.6
---

LTTng features an Apache log4j 1.2 agent, which means your existing
Java applications using log4j 1.2 for logging can record events to
LTTng traces with just a minor source code modification.

<div class="tip">
<p>
    <span class="t">Note:</span>This version of LTTng does not
    support Log4j 2.
</p>
</div>

Here's an example:

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

To compile the snippet above, do:

<pre class="term">
javac -cp /usr/lib/lttng/java/liblttng-ust-agent.jar:$LOG4JCP Test.java
</pre>

where `$LOG4JCP` is the log4j 1.2 JAR file path.

You can run the resulting compiled class like this:

<pre class="term">
java -cp /usr/lib/lttng/java/liblttng-ust-agent.jar:$LOG4JCP:. Test
</pre>
