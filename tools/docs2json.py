#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2015 Philippe Proulx <pproulx@efficios.com>
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
import json
from termcolor import colored


_TOC_PATH = 'toc/docs.yml'
_CONTENTS_ROOT_PATH = 'contents'


class _Link:
    pass


class _IntLink(_Link):
    def __init__(self, section):
        self._section = section

    @property
    def section(self):
        return self._section

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        return self._section == other._section

    def __hash__(self):
        return hash(self._section)

    def to_json(self):
        return {
            'section': self._section,
        }


class _ExtLink(_Link):
    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        return self._url == other._url

    def __hash__(self):
        return hash(self._url)

    def to_json(self):
        return {
            'url': self._url,
        }


class _SectionInfo:
    def __init__(self, path):
        self._path = path
        self._in_links = set()
        self._out_links = set()

    @property
    def path(self):
        return self._path

    @property
    def in_links(self):
        return self._in_links

    @property
    def out_links(self):
        return self._out_links

    def add_in_link(self, link):
        self._in_links.add(link)

    def add_out_link(self, link):
        self._out_links.add(link)

    def to_json(self):
        section_json = {
            'path': self.path,
        }
        in_links_json = []
        out_links_json = []

        for in_link in self.in_links:
            in_links_json.append(in_link.to_json())

        for out_link in self.out_links:
            out_links_json.append(out_link.to_json())

        section_json['in-links'] = in_links_json
        section_json['out-links'] = out_links_json

        return section_json


class _Registry:
    def __init__(self):
        self._section_infos = {}

    def register_section_info(self, sid, section_info):
        self._section_infos[sid] = section_info

    def _resolve_in_links(self):
        for sid in self._section_infos:
            section_info = self._section_infos[sid]
            for out_link in section_info.out_links:
                if type(out_link) != _IntLink:
                    continue

                target_sid = out_link.section
                target_section_info = self._section_infos[target_sid]
                target_section_info.add_in_link(_IntLink(sid))

    def to_json(self):
        self._resolve_in_links()
        sections_json = {}

        for sid, section_info in self._section_infos.items():
            sections_json[sid] = section_info.to_json()

        return json.dumps(sections_json)


def _perror(filename, msg):
    s = '{}  {} {}'.format(filename, colored('Error:', 'red'),
                           colored(msg, 'red', attrs=['bold']))
    print(s, file=sys.stderr)


def _pwarn(filename, msg):
    s = '{}  {} {}'.format(filename, colored('Warning:', 'yellow'),
                           colored(msg, 'yellow', attrs=['bold']))
    print(s, file=sys.stderr)


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
        return

    return ids


_id_re = re.compile(r'^\s*id:\s*([a-zA-Z0-9_-]+)\s*$', flags=re.M)


def _get_sid_from_file(path, c):
    m = _id_re.search(c)

    if not m:
        _perror(path, 'No ID found')
        return

    return m.group(1)


_ilink_re = re.compile(r'\[[^\]]+\]\(([^)]+)\)', flags=re.M)
_elink_re = re.compile(r'<a(?:\s+[^>]+|\s*)>')
_name_re = re.compile(r'name="([^"]+)"')
_href_re = re.compile(r'href="([^"]+)"')
_classes_re = re.compile(r'class="([^"]+)"')


def _register_section_info(registry, toc_ids, path, c):
    sid = _get_sid_from_file(path, c)

    if not sid:
        return False

    ret = True
    ilinks = _ilink_re.findall(c)
    elinks = _elink_re.findall(c)
    section_info = _SectionInfo(path)

    for link in elinks:
        href = _href_re.search(link)
        name = _name_re.search(link)
        classes = _classes_re.search(link)

        if name and not href:
            # simple anchor
            continue

        if classes is None:
            _pwarn(path, 'External link has no "ext" class: "{}"'.format(link))
            classes = []
        else:
            classes = classes.group(1).split(' ')

            if 'int' in classes and 'ext' in classes:
                _pwarn(path, 'External link has both "ext" and "int" classes: "{}"'.format(link))
            elif 'int' not in classes and 'ext' not in classes:
                _pwarn(path, 'External link has no "ext" or "int" class: "{}"'.format(link))

        if href:
            href = href.group(1)

            if href.startswith('#') and 'int' not in classes:
                _pwarn(path, 'External link starts with #: "{}"'.format(href))

            if 'int' in classes:
                ilinks.append(href)
                continue

            section_info.add_out_link(_ExtLink(href))
        elif not name:
            _perror(path, 'External link with no "href" or "name" attribute: "{}"'.format(link))
            ret = False

    for link in ilinks:
        if not link.startswith('#doc-'):
            s = 'Internal link does not start with "#doc-": "{}"'.format(link)
            _perror(path, s)
            ret = False
            continue

        target_sid = link[5:]

        if target_sid not in toc_ids:
            _perror(path, 'Dead internal link: "{}"'.format(link))
            ret = False
        else:
            section_info.add_out_link(_IntLink(target_sid))

    registry.register_section_info(sid, section_info)

    return ret


def _docs2json(toc_ids, contents_files):
    ret = True
    registry = _Registry()

    i = 1

    for path in contents_files:
        with open(path) as f:
            c = f.read()

        ret &= _register_section_info(registry, toc_ids, path, c)

    print(registry.to_json())

    return ret


def _check_non_md(files):
    ret = True

    for f in files:
        if not f.endswith('.md'):
            _perror(f, 'Wrong, non-Markdown file: "{}"'.format(f))
            ret = False

    return ret


def docs2json():
    toc_ids = _get_toc_ids(_TOC_PATH)

    if toc_ids is None:
        return False

    contents_files = _get_files(_CONTENTS_ROOT_PATH)

    if not _check_non_md(contents_files):
        return False

    if not _docs2json(toc_ids, contents_files):
        return False

    return True


if __name__ == '__main__':
    sys.exit(0 if docs2json() else 1)
