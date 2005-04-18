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
Latin language support.

Note: Currently, we assume all cards are lowercase.
"""

import re
import string

from UserDict import UserDict 

_replacement_table = {
    "A": "ā",
    "E": "ē",
    "I": "ī",
    "O": "ō",
    "U": "ū",
}
""" A table of replacement patterns. """

class Convertor(UserDict):
    """ Easy macron maker.

    Your uppercase vowels become long forms. Don't underestimate the
    importance of learning those long vowels. Cause when you're reading out
    loud, you're bound to embarass yoursell.
    
    Like saying e-RU-di-tor instead of ee-ru-DII-tor. What a disaster."""

    def __init__(self):
        self.re = None
        self.regex = None
        UserDict.__init__(self, _replacement_table)
        self._compile()

    def _compile(self): 
        """ Builds a regular expression object based on the keys of the
        dictionary """

        keys = self.keys()
        keys.sort( lambda a,b: len(b)-len(a) )
        
        # Note the first entry -- this lets us specially handle any part that
        # comes between angle brackets. Cf note in __call__.
        tmp = "({(.*?)}|%s)" % "|".join(map(re.escape, keys))
        self.re = tmp
        self.regex = re.compile(self.re)
    
    def __call__(self, mo): 
        """ Handler for each regex match """

        # Grab the matched string, get the related info from the dict.
        matchstr = mo.string[mo.start():mo.end()]
        if matchstr[0] == '{' and matchstr[-1] == '}':
            # It's that special case mentioned above in _compile; strip the
            # angle brackets and return the string without changes.
            unichr = matchstr[1:-1]
        else:
            # Deal with it normally
            unichr = self[matchstr]

        return unichr

    def Convert(self, text): 
        """ Translates and returns the modified text """ 

        # Process text
        return self.regex.sub(self, text)

class Normalizer(UserDict):
    def Convert(self, text): 
        return string.lower(text)

#
# Test routine
#

if __name__ == "__main__":
    """ Read user input and output Unicode latin """
    conv = Convertor()
    norm = Normalizer()
    print "Easy-macron demo (enter 'q' to quit)"
    s = ''
    while 1:
        s = raw_input("> ")
        if s == 'q': break
        print conv.Convert(s)
        print norm.Convert(s)

