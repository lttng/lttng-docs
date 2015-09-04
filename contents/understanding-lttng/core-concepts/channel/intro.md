---
id: channel
---

A _channel_ is a set of events with specific parameters and potential
added context information. Channels have unique names per domain within
a tracing session. A given event is always registered to at least one
channel; having the same enabled event in two channels makes
this event being recorded twice everytime it occurs.

Channels may be individually enabled or disabled. Occurring events of
a disabled channel never make it to recorded events.

The fundamental role of a channel is to keep a shared ring buffer, where
events are eventually recorded by the tracer and consumed by a consumer
daemon. This internal ring buffer is divided into many sub-buffers of
equal size.

Channels, when created, may be fine-tuned thanks to a few parameters,
many of them related to sub-buffers. The following subsections explain
what those parameters are and in which situations you should manually
adjust them.
