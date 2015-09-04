---
id: channel-switch-timer
---

The _switch timer_ period is another important configurable feature of
channels to ensure periodic sub-buffer flushing.

When the _switch timer_ fires, a sub-buffer switch happens. This timer
may be used to ensure that event data is consumed and committed to
trace files periodically in case of a low event throughput:

<script type="text/javascript">
    document.write('<div class="anim img img-50" id="docsvg-channel-switch-timer"></div>');

    $(document).ready(function() {
        var doc = SVG('docsvg-channel-switch-timer');

        doc.viewbox(0, 0, 2, 2);

        var div = 4;
        var evDur = 1000;
        var rb = rbBuildStd(doc, div, 0.97);
        var switchText = doc.text('Switch!');

        switchText.font({
            'size': 0.1,
            'weight': 'bold'
        });
        switchText.center(1, 1);
        switchText.attr({
            'opacity': 0,
            'fill': '#b02b2c'
        });

        var curSubBuf = 0;
        var totalEvents = 0;
        var onEventAdded = function() {
            totalEvents++;

            var curSubBufEvCount = rb.getSubBufEvCount(curSubBuf % div);

            if (totalEvents >= 4) {
                // switch timer fires
                switchText.attr({
                    'opacity': 1
                });
                switchText.animate(500, '<>', 1000).attr({
                    'opacity': 0
                });
                rb.markSubBuf(curSubBuf % div, 'full');

                var lastFullSubBuf = curSubBuf;

                setTimeout(function() {
                    rb.consumeSubBuf(lastFullSubBuf % div);
                }, 3000);
                totalEvents = 0;
                curSubBuf++;
                rb.markSubBuf(curSubBuf % div, 'cur');
            }

            rb.addEvent(curSubBuf % div, evDur, onEventAdded);
        };

        rb.markSubBuf(0, 'cur');
        rb.getGroup().move(1, 1);
        rbSetParentPlayIcon(doc, function() {
            rb.addEvent(0, evDur, onEventAdded);
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

It's also convenient when big sub-buffers are used to cope with
sporadic high event throughput, even if the throughput is normally
lower.
