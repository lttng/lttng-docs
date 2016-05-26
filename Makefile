CONF = asciidoc.html5.conf
PREFIX = lttng-docs
ALLVERSIONS = 2.5 2.6 2.7

ASCIIDOC = asciidoc -v -f $(CONF) -a source-highlighter=pygments
RM = rm -rf

htmldst = $(1)/$(PREFIX)-$(1).html

.PHONY: all

all: $(ALLVERSIONS)

.PHONY: $(ALLVERSIONS)

2.5: $(call htmldst,2.5)

2.6: $(call htmldst,2.6)

2.7: $(call htmldst,2.7)

%.html: %.txt $(CONF)
	$(ASCIIDOC) $<

.PHONY: clean

clean:
	$(RM) $(foreach version,$(ALLVERSIONS),$(call htmldst,$(version)))
