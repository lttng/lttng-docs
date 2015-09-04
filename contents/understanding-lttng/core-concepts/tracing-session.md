---
id: tracing-session
---

A _tracing session_ is&mdash;like any session&mdash;a container of
state. Anything that is done when tracing using LTTng happens in the
scope of a tracing session. In this regard, it is analogous to a bank
website's session: you can't interact online with your bank account
unless you are logged in a session, except for reading a few static
webpages (LTTng, too, can report some static information that does not
need a created tracing session).

A tracing session holds the following attributes and objects (some of
which are described in the following sections):

  * a name
  * the tracing state (tracing started or stopped)
  * the trace data output path/URL (local path or sent over the network)
  * a mode (normal, snapshot or live)
  * the snapshot output paths/URLs (if applicable)
  * for each [domain](#doc-domain), a list of [channels](#doc-channel)
  * for each channel:
    * a name
    * the channel state (enabled or disabled)
    * its parameters (event loss mode, sub-buffers size and count,
      timer periods, output type, trace files size and count, and the rest)
    * a list of added context information
    * a list of [events](#doc-event)
  * for each event:
    * its state (enabled or disabled)
    * a list of instrumentation points (tracepoints, system calls,
      dynamic probes, other types of probes)
    * associated log levels
    * a filter expression

All this information is completely isolated between tracing sessions.

Conceptually, a tracing session is a per-user object; the
[Plumbing](#doc-plumbing) section shows how this is actually
implemented. Any user may create as many concurrent tracing sessions
as desired. As you can see in the list above, even the tracing state
is a per-tracing session attribute, so that you may trace your target
system/application in a given tracing session with a specific
configuration while another one stays inactive.

The trace data generated in a tracing session may be either saved
to disk, sent over the network or not saved at all (in which case
snapshots may still be saved to disk or sent to a remote machine).
