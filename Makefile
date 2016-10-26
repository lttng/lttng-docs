# Copyright 2016 Philippe Proulx <pproulx@efficios.com>

CONF = asciidoc.html5.conf
PREFIX = lttng-docs
ALLVERSIONS = $(sort $(wildcard 2.*))

ASCIIDOC = asciidoc -v -f $(CONF) -a source-highlighter=pygments
RM = rm -rf

define vrule
$(1)/$(PREFIX)-$(1).html: $(1)/$(PREFIX)-$(1).txt $(CONF)
	$(ASCIIDOC) -a "lttng_version=$(1)" $(1)/$(PREFIX)-$(1).txt

.PHONY: $(1)

$(1): $(1)/$(PREFIX)-$(1).html
endef

.PHONY: all

all: $(ALLVERSIONS)

$(foreach v,$(ALLVERSIONS),$(eval $(call vrule,$(v))))

.PHONY: clean

clean:
	$(RM) $(foreach v,$(ALLVERSIONS),$(v)/$(PREFIX)-$(v).html)
