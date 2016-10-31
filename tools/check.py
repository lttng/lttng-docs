# The MIT License (MIT)
#
# Copyright (c) 2016 Philippe Proulx <pproulx@efficios.com>
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

from termcolor import colored
import lxml.etree as etree
import subprocess
import argparse
import os.path
import sys
import os


def _perror(msg, exit=True):
    print('{} {}'.format(colored('Error:', 'red'), colored(msg, 'red', attrs=['bold'])),
          file=sys.stderr)

    if exit:
        sys.exit(1)


def _pinfo(msg):
    print('{} {}'.format(colored('::', 'blue'), colored(msg, 'blue', attrs=['bold'])))


def _get_script_dir():
    return os.path.dirname(os.path.realpath(__file__))


class _Checker:
    def __init__(self, infile, verbose):
        self._infile = infile
        self._verbose = verbose
        self._has_error = False
        self._set_paths()
        self._pverbose('asciidoc -> DocBook')
        self._build()
        self._set_root()
        self._check()

    @property
    def has_error(self):
        return self._has_error

    def _pverbose(self, msg):
        if self._verbose:
            _pinfo(msg)

    def _perror(self, msg, fatal=False):
        self._has_error = True
        _perror(msg, fatal)

    def _set_paths(self):
        self._indir = os.path.dirname(self._infile)
        self._imgexportdir = os.path.join(self._indir, 'images', 'export')
        self._builddir = os.path.join(_get_script_dir(), 'check', os.path.basename(self._infile))
        self._outfile = os.path.join(self._builddir, 'out.xml')

    def _build(self):
        conf = os.path.join(_get_script_dir(), 'asciidoc.check.conf')
        os.makedirs(self._builddir, mode=0o755, exist_ok=True)
        cmd = [
            'asciidoc',
            '-f', conf,
            '-b', 'docbook',
            '-o', self._outfile,
        ]

        if self._verbose:
            cmd.append('-v')

        cmd.append(self._infile)
        res = subprocess.run(cmd)

        if res.returncode != 0:
            self._perror('asciidoc did not finish successfully', True)

    def _set_root(self):
        tree = etree.ElementTree(file=self._outfile)
        self._root = tree.getroot()

    def _check(self):
        self._pverbose('Checking links')
        self._check_links()
        self._pverbose('Checking images')
        self._check_images()

    def _check_links(self):
        sections_anchors = self._root.findall('.//section')
        sections_anchors += self._root.findall('.//anchor')
        sections_anchors += self._root.findall('.//glossary')
        sections_anchors += self._root.findall('.//important')
        sections_anchors += self._root.findall('.//tip')
        sections_anchors += self._root.findall('.//caution')
        sections_anchors += self._root.findall('.//warning')
        sections_anchors += self._root.findall('.//note')
        links = self._root.findall('.//link')
        end_ids = set()

        for sa in sections_anchors:
            end_id = sa.get('id')

            if sa.tag in ('section', 'anchor') and end_id is None:
                self._perror('Found a section/anchor with no ID', True)

            end_ids.add(end_id)

        link_ends = set()

        for link in links:
            end = link.get('linkend')

            if end is None:
                self._perror('Found a link with no end', True)

            link_ends.add(end)

        has_error = False

        for end in link_ends:
            if end not in end_ids:
                self._perror('Link end "{}" does not name a section/anchor ID'.format(end))

    def _check_images(self):
        image_datas = self._root.findall('.//imagedata')

        for image_data in image_datas:
            fileref = image_data.get('fileref')
            path = os.path.join(self._imgexportdir, fileref)

            if not os.path.isfile(path):
                self._perror('Cannot find image "{}"'.format(fileref))


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('infile')
    args = parser.parse_args()

    if not os.path.isfile(args.infile):
        _perror('"{}" is not an existing file'.format(args.infile))

    return args


def _main():
    args = _parse_args()
    checker = _Checker(args.infile, args.verbose)

    if checker.has_error:
        return 1

    print(colored('All good!', 'green', attrs=['bold']))

    return 0


if __name__ == '__main__':
    sys.exit(_main())
