---
id: python-application
since: 2.7
---

Python 2 and Python 3 applications using the standard
<a href="https://docs.python.org/3/howto/logging.html" class="ext"><code>logging</code> module</a>
can be traced by LTTng using the LTTng-UST Python agent.

Import the `lttngust` package in your Python application. For example:

~~~ python
import lttngust
import logging
import time


def example():
    logging.basicConfig()
    logger = logging.getLogger('my-logger')

    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(1)


if __name__ == '__main__':
    example()
~~~

Importing `lttngust` adds a logging handler which emits LTTng-UST
events. You do not need to get a special logger for tracing to work.

Note that `logging.basicConfig()`, which adds to the root logger a basic
logging handler which prints to the standard error stream, is not
strictly required for LTTng-UST tracing to work, but in versions of
Python preceding 3.2, a warning message could be seen indicating that no
handler exists for the logger `my-logger`.

Use the `--python` option of the `lttng enable-event`,
`lttng disable-event`, and `lttng list` commands to target
Python applications. For example, here's how to enable the events
produced by the Python logger above:

<pre class="term">
lttng enable-event --python my-logger
</pre>

Standard Python log levels are supported using the `PYTHON_` prefix.
For example, here's how to enable the warning (and more important)
events produced by the Python logger above:

<pre class="term">
lttng enable-event --python my-logger --loglevel PYTHON_WARNING
</pre>

See [Enabling and disabling events](#doc-enabling-disabling-events) for
more options.

When loading, the LTTng-UST Python agent tries to register to the
[session daemon](#doc-lttng-sessiond). Note that the session daemon
needs to be started _before_ the Python application is started. If a
session daemon is found, the agent tries to register to it during
5&nbsp;seconds, after which the application continues without LTTng
tracing support. This timeout value is overriden by the
`LTTNG_UST_PYTHON_REGISTER_TIMEOUT` environment variable (milliseconds).

If the session daemon stops while a registered Python application is
registered, the application retries to connect and register to a session
daemon every 3&nbsp;seconds. This timeout value is overridden by the
`LTTNG_UST_PYTHON_REGISTER_RETRY_DELAY` environment variable.
