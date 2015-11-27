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
import graphviz


def _get_section_infos(json_path):
    with open(json_path) as f:
        c = f.read()

    return json.loads(c)


def dotlinks():
    section_infos = _get_section_infos(sys.argv[1])
    digraph = graphviz.Digraph(format='png', engine='dot')
    digraph.attr('node', fontname='Terminus', fontsize='8')

    for sid, section_info in section_infos.items():
        color = ''
        style = ''
        in_links_count = len(section_info['in-links'])
        out_links_count = len(section_info['out-links'])

        if in_links_count == 0 and out_links_count == 0:
            color = '#e62739'
        elif in_links_count == 0:
            color = '#fae596'
        elif out_links_count == 0:
            color = '#6ed3cf'

        if color:
            style = 'filled'

        digraph.node(sid, style=style, color=color)

    for sid, section_info in section_infos.items():
        out_links = section_info['out-links']

        for out_link in out_links:
            if 'section' in out_link:
                dest = out_link['section']
                digraph.edge(sid, dest)

    digraph.render(filename='linkgraph')

    return True


if __name__ == '__main__':
    sys.exit(0 if dotlinks() else 1)
