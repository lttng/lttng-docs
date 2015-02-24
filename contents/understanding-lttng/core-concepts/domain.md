---
id: domain
---

A tracing _domain_ is the official term the LTTng project uses to
designate a tracer category.

There are currently four known domains:

  * Linux kernel
  * user space
  * `java.util.logging` (JUL)
  * log4j

Different tracers expose common features in their own interfaces, but,
from a user's perspective, you still need to target a specific type of
tracer to perform some actions. For example, since both kernel and user
space tracers support named tracepoints (probes manually inserted in
source code), you need to specify which one is concerned when enabling
an event because both domains could have existing events with the same
name.

Some features are not available in all domains. Filtering enabled
events using custom expressions, for example, is currently not
supported in the kernel domain, but support could be added in the
future.
