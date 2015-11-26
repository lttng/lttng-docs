---
id: preface
---

<div class="copyright">
    <p>
        Copyright © 2014-2015 The LTTng Project
    </p>

    <p>
        This work is licensed under a
        <a class="ext" href="http://creativecommons.org/licenses/by/4.0/">Creative
        Commons Attribution 4.0 International License</a>.
    </p>
</div>


## Welcome!

Welcome to the **LTTng Documentation**!

The _Linux Trace Toolkit: next generation_
is an open source system software package for correlated tracing of the
Linux kernel, user applications and libraries. LTTng consists of kernel
modules (for Linux kernel tracing) and dynamically loaded libraries (for
user application and library tracing). It is controlled by a session
daemon, which receives commands from a command line interface.


### Convention

Function and argument names, variable names, command names,
file system paths, file names and other precise strings are written
using a <code>monospaced typeface</code> in this document. An
<code><em>italic</em> word</code> within such a block is a
placeholder, usually described in the following sentence.

Practical tips and sidenotes are given throughout the document using a
blue background:

<div class="tip">
<p><span class="t">Tip:</span>Make sure you read the tips.</p>
</div>

Terminal boxes are used to show command lines:

<pre class="term">
echo This is a terminal box
</pre>

Typical command prompts, like `$` and `#`, are not shown in terminal
boxes to make copy/paste operations easier, especially for multiline
commands which may be copied and pasted as is in a user's terminal.
Commands to be executed as a root user begin with `sudo`.


### Target audience

The material of this documentation is appropriate for intermediate to
advanced software developers working in a Linux environment who are
interested in efficient software tracing. LTTng may also be worth a
try for students interested in the inner mechanics of their systems.

Readers who do not have a programming background may wish to skip
everything related to instrumentation, which requires, most of the
time, some programming language skills.

<div class="tip">
<p><span class="t">Note to readers:</span>This is an <strong>open
documentation</strong>: its source is available in a
<a class="ext" href="https://github.com/lttng/lttng-docs">public Git
repository</a>. Should you find any error in the contents of this text,
any grammatical mistake, or any dead link, we would be very grateful if
you would fill a GitHub issue for it or, even better, contribute a patch
to this documentation by creating a pull request.</p>
</div>

### Chapter descriptions

What follows is a list of brief descriptions of this documentation's
chapters. The latter are ordered in such a way as to make the reading
as linear as possible.

  1. [Nuts and bolts](#doc-nuts-and-bolts) explains the
     rudiments of software tracing and the rationale behind the
     LTTng project.
  2. [Installing LTTng](#doc-installing-lttng) is divided into
     sections describing the steps needed to get a working installation
     of LTTng packages for common Linux distributions and from its
     source.
  3. [Getting started](#doc-getting-started) is a very concise guide to
     get started quickly with LTTng kernel and user space tracing. This
     chapter is recommended if you're new to LTTng or to software tracing
     in general.
  4. [Understanding LTTng](#doc-understanding-lttng) deals with some
     core concepts and components of the LTTng suite. Understanding
     those is important since the next chapter assumes you're familiar
     with them.
  5. [Using LTTng](#doc-using-lttng) is a complete user guide of the
     LTTng project. It shows in great details how to instrument user
     applications and the Linux kernel, how to control tracing sessions
     using the `lttng` command line tool, and miscellaneous practical use
     cases.
  6. [Reference](#doc-reference) contains references of LTTng components.

We recommend that you read the above chapters in this order, although
some of them may be skipped depending on your situation. You may skip
[Nuts and bolts](#doc-nuts-and-bolts) if you're familiar with tracing
and the LTTng project. Also, you may jump over
[Installing LTTng](#doc-installing-lttng) if LTTng is already properly
installed on your target system.


### Acknowledgements

A few people made the online LTTng Documentation possible.

Philippe Proulx wrote and formatted most of the text.
Daniel U. Thibault, from the
<abbr title="Defence Research and Development Canada">DRDC</abbr>,
wrote an open guide called <em>LTTng: The Linux Trace Toolkit Next
Generation&nbsp;&mdash;&nbsp;A Comprehensive User's Guide (version 2.3
edition)</em> which was mostly used to complete parts of the
[Understanding LTTng](#doc-understanding-lttng) chapter and for a few
passages here and there.
The whole <a href="http://www.efficios.com/" class="ext">EfficiOS</a>
team (Christian Babeux, Antoine Busque, Julien Desfossez,
Mathieu Desnoyers, Jérémie Galarneau and David Goulet) made essential
reviews of the whole document.

We sincerely thank everyone who helped make this documentation what
it is. We hope you enjoy reading it as much as we did writing it.
