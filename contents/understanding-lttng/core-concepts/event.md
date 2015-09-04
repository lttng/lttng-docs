---
id: event
---

An _event_, in LTTng's realm, is a term often used metonymically,
having multiple definitions depending on the context:

  1. When tracing, an event is a _point in space-time_. Space, in a
     tracing context, is the set of all executable positions of a
     compiled application by a logical processor. When a program is
     executed by a processor and some instrumentation point, or
     _probe_, is encountered, an event occurs. This event is accompanied
     by some contextual payload (values of specific variables at this
     point of execution) which may or may not be recorded.
  2. In the context of a recorded trace file, the term _event_ implies
     a _recorded event_.
  3. When configuring a tracing session, _enabled events_ refer to
     specific rules which could lead to the transfer of actual
     occurring events (1) to recorded events (2).

The whole [Core concepts](#doc-core-concepts) section focuses on the
third definition. An event is always registered to _one or more_
channels and may be enabled or disabled at will per channel. A disabled
event never leads to a recorded event, even if its channel is enabled.

An event (3) is enabled with a few conditions that must _all_ be met
when an event (1) happens in order to generate a recorded event (2):

  1. A _probe_ or group of probes in the traced application must be
     executed.
  2. **Optionally**, the probe must have a log level matching a
     log level range specified when enabling the event.
  3. **Optionally**, the occurring event must satisfy a custom
     expression, or _filter_, specified when enabling the event.

The following illustration summarizes how tracing sessions, domains,
channels and events are related:

<div class="img img-90">
<object data="/images/docs26/core-concepts.svg" type="image/svg+xml">
  <img src="/images/docs26/core-concepts.svg">
</object>
</div>

This diagram also shows how events may be individually enabled/disabled
(green/grey) and how a given event may be registered to more than one
channel.
