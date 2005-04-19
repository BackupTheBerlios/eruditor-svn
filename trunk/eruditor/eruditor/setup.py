#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# $Id$

VERSION = '0.1.0'

from distutils.core import setup
import sys, glob

py2exe_options = {
    "py2exe": {"packages": "encodings"}
}

if sys.platform == 'darwin':
    import py2app
    EXTRA = dict(app = ['Eruditor.py'])
elif sys.platform == 'win32':
    import py2exe
    EXTRA = dict(
	    windows = [{'script':'Eruditor.py'}],
	    options = py2exe_options,
    )
else:
    print """\
This setup script only supports:
  - py2app on Mac OS X
  - py2exe on Windows"""
    sys.exit(0)

setup(
    name = 'eruditor',
    version = VERSION,
    description = 'ērudītor -- A Vocabulary Trainer',
    long_description = """\
A card-based learning system for use with Greek, Latin, and other
languages.""",
    url = 'http://eruditor.berlios.de/',
    author = 'Alexander Lee',
    author_email = 'alexanderlee@users.berlios.de',
    license = 'GPL (see COPYING)',
    platforms = 'OS-independent',
    data_files = [('img', glob.glob('img/*.png'))],
    **EXTRA
)
