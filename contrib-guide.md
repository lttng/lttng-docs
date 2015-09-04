Contributor's guide
===================

This guide presents the structure and conventions of the LTTng
Documentation's source. Make sure you read it thoroughly before
contributing a change.


Branches
--------

The online documentation published at <http://lttng.org/docs/> is always
compiled from the sources of this repository's latest stable branch.
The `master` branch contains the current documentation of the upcoming
LTTng release.


Structure of sources
--------------------

`toc/docs.yml` is a YAML tree of all chapters, sections and subsections.
It indicates which unique ID is linked to which position in the
hierarchy and its true title.

In the `contents` directory, the `preface.md` file is the preface contents.
Each chapter has its own directory (directory names are not significant).
Within those, `intro.md` files are partial introductions and then each
section has its own directory, and so on, unless a section has no
subsections, in which case all its contents is in a single Markdown file
named _more or less_ like its ID.

Each Markdown file begins with a YAML front matter which only contains
the unique ID of this chapter/section:

```yaml
---
id: unique-id-goes-here
---

First paragraph goes here.
```

Editable image sources are placed in `images/src` and their rendered
equivalents are located in `images/export`.

`tools/checkdocs.py` is a Python 3 script which may be used to find
typical errors in the whole documentation (dead internal links,
common grammar mistakes, etc.). It needs the
[`termcolor`](https://pypi.python.org/pypi/termcolor) Python package.
Run it from the repository's root:

    tools/checkdocs.py

and it will potentially output a list of errors and warnings.


Format of sources
-----------------

The sources are made of a fusion of Markdown and HTML processed by
[kramdown](http://kramdown.gettalong.org/). Markdown is preferred,
HTML being only used for specific cases that need special formatting
not available using plain Markdown. The kramdown processor is clever
enough to support both languages in the same file, even in the same
paragraph!


### HTML specifics

Here's a list of HTML blocks and inline code used throughout the
document. If you need to contribute, please use them when needed to
preserve the document's visual consistency.


#### Tip/note/warning/error blocks

Tip/note block:

```html
<div class="tip">
    <p>
        <span class="t">Title goes here followed by colon:</span>Text goes
        here; plain HTML.
    </p>
    <p>
        Multiple paragraphs is allowed.
    </p>
</div>
```

Title should be `Tip:` for a tip and `Note:` for a note.



#### External links

Internal links should always use Markdown
(`[caption](#doc-section)`). External links, however, need a special
style and must use the `<a>` tag with the `ext` CSS class:

```html
The LTTng Documentation is
<a href="https://github.com/lttng/lttng-docs" class="ext">public</a>.
```

Sometimes, however, it is necessary to write internal links in plain
HTML, for example in tip blocks, since Markdown code is not processed.
In these cases, add the `int` CSS class as a hint to prevent the static
analyzer from complaining (`tools/checkdocs.py`).


#### Abbreviations

Use `<abbr>` for describing abbreviations. This should only be used
for the first use of the abbreviation:

```html
The <abbr title="Linux Trace Toolkit: next generation">LTTng</abbr>
project is an open source system software package [...]
```


#### Non-breaking spaces

Sometimes, a non-breaking space HTML entity (`&nbsp;`) needs to be
explicitly written.

Examples:

```html
The size of this file is 1039&nbsp;bytes.

This integer is displayed in base&nbsp;16.

A check is performed every 3000&nbsp;ms.
```


#### Placeholders in inline code

You must use `<em>` to emphasize a placeholder within a `<code>` tag
because Markdown backticks (<code>`</code>) always render their
content literally:

```html
Name your file <code>something_<em>sys</em>.c</code>, where
<code><em>sys</em></code> is your system name.
```


#### Terminal boxes

A terminal box, where command lines are shown, is a simple `<pre>`
with the `term` class:

```html
<pre class="term">
echo This is a terminal box
</pre>
```

Do not prefix command lines with prompts (`$`/`#`) since this makes
copy/paste operations painful.

You may use `<strong>` tags to emphasize a part of the command line:

```html
<pre class="term">
echo This is a <strong>terminal</strong> box
</pre>
```

Results of commands, if needed, should be presented in a simple
`text` kramdown code block:

<pre>
~~~ text
[15:30:34.835895035] (+?.?????????) hostname hello_world: { cpu_id = 1 }, { my_int = 8, char0 = 68, char1 = 97, product = "DataTraveler 2.0" }
[15:30:42.262781421] (+7.426886386) hostname hello_world: { cpu_id = 1 }, { my_int = 9, char0 = 80, char1 = 97, product = "Patriot Memory" }
[15:30:48.175621778] (+5.912840357) hostname hello_world: { cpu_id = 1 }, { my_int = 10, char0 = 68, char1 = 97, product = "DataTraveler 2.0" }
~~~
</pre>


#### Images

Use

```html
<div class="img img-70">
    <img src="/images/docs26/image-name.png" alt="Short description">
</div>
```

to display an image. Change `img-70` to `img-` followed by the
width percentage you wish.

The SVG format is preferred. In this case, use the `<object>` tag to
render an interactive SVG, with an inner raster image fallback for
basic browsers:

```html
<div class="img img-90">
  <object data="/images/docs26/image-name.svg" type="image/svg+xml">
    <img src="/images/docs26/image-name.png" alt="Short description">
  </object>
</div>
```

An interactive SVG object allows its text to be selected, amongst other
features.


Convention
----------

A few rules to comply with in order to keep the text as
consistent as possible:

  * Use _user space_, not _userspace_ nor _user-space_.
    (neither _user land_).
  * Use _file system_, not _filesystem_.
  * Use _use case_, not _use-case_ nor _usecase_.
  * Use _the C standard library_, not _libc_.
  * Use _log level_, not _loglevel_.
  * Use complete LTTng project names: _LTTng-modules_, _LTTng-UST_ and
    _LTTng-tools_, not _modules_, _UST_ and _tools_.
  * All code snippets should use 4 spaces for indentation (even C)
    so that they are not too large.
  * Prefer emphasis (Markdown: `_something_`, HTML: `<em>something</em>`)
    to strong (Markdown: `**something**`, HTML: `<strong>something</strong>`)
    for emphasizing text.
  * Try to stay behind the 72th column mark if possible, and behind
    the 80th column otherwise.
  * Do not end directory paths with a forward slash
    (good: `include/trace/events`, bad: `include/trace/events/`).
  * Keep the text as impersonal as possible (minimize the use of
    _I_, _we_, _us_, etc.), except for user guides/tutorials where
    _we_ have an ongoing example.


Committing
----------

If you make a change to a single contents file, prefix your Git commit
message's first line with the file ID followed by `: `, e.g:

    archlinux: minor fix
