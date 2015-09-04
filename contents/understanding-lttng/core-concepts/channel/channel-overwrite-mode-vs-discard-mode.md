---
id: channel-overwrite-mode-vs-discard-mode
---

As previously mentioned, a channel's ring buffer is divided into many
equally sized sub-buffers.

As events occur, they are serialized as trace data into a specific
sub-buffer (yellow arc in the following animation) until it is full:
when this happens, the sub-buffer is marked as consumable (red) and
another, _empty_ (white) sub-buffer starts receiving the following
events. The marked sub-buffer will be consumed eventually by a consumer
daemon (returns to white).

<script type="text/javascript">
    document.write('<div class="anim img img-50" id="docsvg-channel-subbuf-anim"></div>');

    $(document).ready(function() {
        var doc = SVG('docsvg-channel-subbuf-anim');

        doc.viewbox(0, 0, 2, 2);

        var stdRb = rbBuildStdAnimated(doc, {
            div: 5,
            oR: 0.97,
            evDur: 300,
            evPerSubBuf: 6,
            consumerAfter: 10
        });

        stdRb.rb.getGroup().move(1, 1);
        rbSetParentPlayIcon(doc, function() {
            rbStdStart(stdRb);
        });
    });
</script>

<noscript>
    <div class="err">
        <p>
            <span class="t">Oops!</span>JavaScript must be enabled in
            order to view animations.
        </p>
    </div>
</noscript>

In an ideal world, sub-buffers are consumed faster than filled, like it
is the case above. In the real world, however, all sub-buffers could be
full at some point, leaving no space to record the following events. By
design, LTTng is a _non-blocking_ tracer: when no empty sub-buffer
exists, losing events is acceptable when the alternative would be to
cause substantial delays in the instrumented application's execution.
LTTng privileges performance over integrity, aiming at perturbing the
traced system as little as possible in order to make tracing of subtle
race conditions and rare interrupt cascades possible.

When it comes to losing events because no empty sub-buffer is available,
the channel's _event loss mode_ determines what to do amongst:

  * **Discard**: drop the newest events until a sub-buffer is released.
  * **Overwrite**: clear the sub-buffer containing the oldest recorded
    events and start recording the newest events there. This mode is
    sometimes called _flight recorder mode_ because it behaves like a
    flight recorder: always keep a fixed amount of the latest data.

Which mechanism you should choose depends on your context: prioritize
the newest or the oldest events in the ring buffer?

Beware that, in overwrite mode, a whole sub-buffer is abandoned as soon
as a new event doesn't find an empty sub-buffer, whereas in discard
mode, only the event that doesn't fit is discarded.

Also note that a count of lost events will be incremented and saved in
the trace itself when an event is lost in discard mode, whereas no
information is kept when a sub-buffer gets overwritten before being
committed.

There are known ways to decrease your probability of losing events. The
next section shows how tuning the sub-buffers count and size can be
used to virtually stop losing events.
