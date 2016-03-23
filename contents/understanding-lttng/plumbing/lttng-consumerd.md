---
id: lttng-consumerd
---

The _consumer daemon_, or `lttng-consumerd`, is a program sharing some
ring buffers with user applications or the LTTng kernel modules to
collect trace data and output it at some place (on disk or sent over
the network to an LTTng relay daemon).

Consumer daemons are created by a session daemon as soon as events are
enabled within a tracing session, well before tracing is activated
for the latter. Entirely managed by session daemons,
consumer daemons survive session destruction to be reused later,
should a new tracing session be created. Consumer daemons are always
owned by the same user as their session daemon. When its owner session
daemon is killed, the consumer daemon also exits. This is because
the consumer daemon is always the child process of a session daemon.
Consumer daemons should never be started manually. For this reason,
they are not installed in one of the usual locations listed in the
`PATH` environment variable. `lttng-sessiond` has, however, a
<a href="/man/8/lttng-sessiond/v2.7" class="ext">bunch of options</a> to
specify custom consumer daemon paths if, for some reason, a consumer
daemon other than the default installed one is needed.

There are up to two running consumer daemons per user, whereas only one
session daemon may run per user. This is because each process has
independent bitness: if the target system runs a mixture of 32-bit and
64-bit processes, it is more efficient to have separate corresponding
32-bit and 64-bit consumer daemons. The `root` user is an exception: it
may have up to _three_ running consumer daemons: 32-bit and 64-bit
instances for its user space applications and one more reserved for
collecting kernel trace data.

As new tracing domains are added to LTTng, the development community's
intent is to minimize the need for additionnal consumer daemon instances
dedicated to them. For instance, the `java.util.logging` (JUL) domain
events are in fact mapped to the user space domain, thus tracing this
particular domain is handled by existing user space domain consumer
daemons.
