---
id: channel-subbuf-size-vs-subbuf-count
---

For each channel, an LTTng user may set its number of sub-buffers and
their size.

Note that there is a noticeable tracer's CPU overhead introduced when
switching sub-buffers (marking a full one as consumable and switching
to an empty one for the following events to be recorded). Knowing this,
the following list presents a few practical situations along with how
to configure sub-buffers for them:

  * **High event throughput**: in general, prefer bigger sub-buffers to
    lower the risk of losing events. Having bigger sub-buffers will
    also ensure a lower sub-buffer switching frequency. The number of
    sub-buffers is only meaningful if the channel is in overwrite mode:
    in this case, if a sub-buffer overwrite happens, you will still have
    the other sub-buffers left unaltered.
  * **Low event throughput**: in general, prefer smaller sub-buffers
    since the risk of losing events is already low. Since events
    happen less frequently, the sub-buffer switching frequency should
    remain low and thus the tracer's overhead should not be a problem.
  * **Low memory system**: if your target system has a low memory
    limit, prefer fewer first, then smaller sub-buffers. Even if the
    system is limited in memory, you want to keep the sub-buffers as
    big as possible to avoid a high sub-buffer switching frequency.

You should know that LTTng uses CTF as its trace format, which means
event data is very compact. For example, the average LTTng Linux kernel
event weights about 32&nbsp;bytes. A sub-buffer size of 1&nbsp;MiB is
thus considered big.

The previous situations highlight the major trade-off between a few big
sub-buffers and more, smaller sub-buffers: sub-buffer switching
frequency vs. how much data is lost in overwrite mode. Assuming a
constant event throughput and using the overwrite mode, the two
following configurations have the same ring buffer total size:

<script type="text/javascript">
    document.write('<div class="anim img img-100" id="docsvg-channel-subbuf-size-vs-count-anim"></div>');

    $(document).ready(function() {
        var doc = SVG('docsvg-channel-subbuf-size-vs-count-anim');

        doc.viewbox(0, 0, 4.25, 2);

        var stdRb2 = rbBuildStdAnimated(doc, {
            div: 2,
            oR: 0.97,
            evDur: 300,
            evPerSubBuf: 17,
            consumerAfter: 25
        });
        var stdRb16 = rbBuildStdAnimated(doc, {
            div: 8,
            oR: 0.97,
            evDur: 300,
            evPerSubBuf: 4,
            consumerAfter: 6
        });

        stdRb2.rb.getGroup().move(1, 1);
        stdRb16.rb.getGroup().move(3.25, 1);
        rbSetParentPlayIcon(doc, function() {
            rbStdStart(stdRb2);
            rbStdStart(stdRb16);
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

  * **2 sub-buffers of 4 MiB each** lead to a very low sub-buffer
    switching frequency, but if a sub-buffer overwrite happens, half of
    the recorded events so far (4&nbsp;MiB) are definitely lost.
  * **8 sub-buffers of 1 MiB each** lead to 4&nbsp;times the tracer's
    overhead as the previous configuration, but if a sub-buffer
    overwrite happens, only the eighth of events recorded so far are
    definitely lost.

In discard mode, the sub-buffers count parameter is pointless: use two
sub-buffers and set their size according to the requirements of your
situation.
