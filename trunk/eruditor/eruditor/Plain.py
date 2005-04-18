# -*- coding: utf-8 -*-
#
# File: $Id$
# Author: Alexander Lee
#
# Eruditor (ērudītor), a card-based vocabulary training program
# Copyright (C) 2005 Alexander Lee
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
Provides plain language support.
Raw Unicode text with no applied conversions.
"""

import string

class Convertor(object):
    """ A do-nothing convertor class. """
    def Convert(self, text):
        """ Do nothing """
        return text

class Normalizer(object):
    """ A plain normalizer class. Simply lower-cases the text. """
    def Convert(self, text): 
        return string.lower(text)

