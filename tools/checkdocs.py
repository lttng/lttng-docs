#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2014 Philippe Proulx <eepp.ca>
# Copyright (c) 2014 The LTTng Project <lttng.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import os
import sys
from termcolor import colored


TOC_PATH = 'toc/docs.yml'
CONTENTS_ROOT_PATH = 'contents'


def _perror(filename, msg):
    s = '{}  {} {}'.format(filename, colored('Error:', 'red'),
                           colored(msg, 'red', attrs=['bold']))
    print(s)


def _pwarn(filename, msg):
    s = '{}  {} {}'.format(filename, colored('Warning:', 'yellow'),
                           colored(msg, 'yellow', attrs=['bold']))
    print(s)


def _get_files(root):
    files = []

    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            files.append(os.path.join(dirpath, f))

    return sorted(files)


def _get_toc_ids(path):
    p = re.compile(r'id\s*:\s*(.+)$', flags=re.M)

    with open(path) as f:
        orig_ids = p.findall(f.read())

    ids = set(orig_ids)

    if len(ids) != len(orig_ids):
        _perror(path, 'Duplicate IDs')
        return None

    return ids


def _check_file_links(toc_ids, path, c):
    ilinkp = re.compile(r'\[[^\]]+\]\(([^)]+)\)', flags=re.M)
    elinkp = re.compile(r'<a(?:\s+[^>]+|\s*)>')

    ret = True

    ilinks = ilinkp.findall(c)
    elinks = elinkp.findall(c)

    for link in ilinks:
        if not link.startswith('#doc-'):
            s = 'Internal link does not start with "#doc-": "{}"'.format(link)
            _perror(path, s)
            ret = False
            continue

        sid = link[5:]

        if sid not in toc_ids:
            _perror(path, 'Dead internal link: "{}"'.format(link))
            ret = False

    hrefp = re.compile(r'href="([^"]+)"')
    classesp = re.compile(r'class="([^"]+)"')

    for link in elinks:
        href = hrefp.search(link)
        classes = classesp.search(link)

        if classes is None:
            _pwarn(path, 'External link has no "ext" class: "{}"'.format(link))
        else:
            classes = classes.group(1).split(' ')

            if 'int' not in classes and 'ext' not in classes:
                _pwarn(path, 'External link has no "ext" class: "{}"'.format(link))

        if href is not None:
            if href.group(1).startswith('#') and 'int' not in classes:
                _pwarn(path, 'External link starts with #: "{}"'.format(href.group(1)))
        else:
            _perror(path, 'External link with no "href": "{}"'.format(link))
            ret = False

    return ret


def _check_contents(toc_ids, contents_files):
    ret = True

    for path in contents_files:
        with open(path) as f:
            c = f.read()

        ret &= _check_file_links(toc_ids, path, c)

    return ret


def _check_non_md(files):
    ret = True

    for f in files:
        if not f.endswith('.md'):
            _perror(f, 'Wrong, non-Markdown file')
            ret = False

    return ret


def checkdocs():
    toc_ids = _get_toc_ids(TOC_PATH)

    if toc_ids is None:
        return False

    contents_files = _get_files(CONTENTS_ROOT_PATH)

    if not _check_non_md(contents_files):
        return False

    if not _check_contents(toc_ids, contents_files):
        return False

    return True


if __name__ == '__main__':
    sys.exit(0 if checkdocs() else 1)
