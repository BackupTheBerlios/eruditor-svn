# -*- coding: utf-8 -*-
#
# Eruditor (ērudītor), a card-based vocabulary training program
# Copyright (C) 2005 Alexander Lee
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# File: Greek.py
# Author: Alexander Lee
#
# Greek language support.

import re
import string

from UserDict import UserDict 

import GreekPatterns

_replacement_table = GreekPatterns.BETACODE_ALT
""" A table of replacement patterns.
Each key is the betacode representation of one Unicode character.
Each value is a tuple containing: (a) the Unicode value, and (b) additional
information that must be appended.

What is part (b) for, anyway? Well, sometimes we'll have a long vowel (alpha,
iota, or upsilon) with diacritics. Since the precombined Unicode characters
with diacritics do not have indications of vowel length, we'll need to append a
listing these vowels at the end. For instance:

    poli_/ths --> πολίτης [ῑ] """

_cmp_table = GreekPatterns.BETACODE_CMP

class Convertor(UserDict):
    """ Convertor from ASCII Beta Code to Unicode Greek text.

    Adapted from Python Cookbook recipe 81330. Thanks to Xavier Defrang and
    all comment posters.

    For the most part this conversion follows TLG Beta Code,
    http://www.tlg.uci.edu/BetaCode.html, with the following
    differences:

    1. Use of lowercase letters.
    2. Don't require asterisks.

    For alpha, iota, and upsilon, remember your long marks! The convertor will
    append a long/short indicator if a long/short vowel has diacritics (such as
    in the LSJ). """

    def __init__(self):
        self.re = None
        self.regex = None

        # Enter all betacode replacements into this dict
        UserDict.__init__(self, _replacement_table)

        # Go ahead and compile it
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
            (unichr, additional) = self[matchstr]

            # If there's additional info for this match, append it to the
            # string in which we're collecting such info.
            # FIXME suppressing these for now until these replacements are done
            # on a word-by-word basis
            #if additional > "":
            #    self.addstr += additional

        return unichr
    
    def Convert(self, text): 
        """ Translates and returns the modified text """ 

        # Hack to get final sigma substitution working...
        text += "$"

        # Reset string for additional data
        self.addstr = ""
        
        # Process text
        result = self.regex.sub(self, text)
        if self.addstr != "":
            result += " [%s]" % self.addstr
        return result

class Normalizer(UserDict):
    """ Convertor from ASCII Beta Code to simple cmp()-arable ASCII. """

    def __init__(self):
        self.re = None
        self.regex = None

        # Enter all betacode replacements into this dict
        UserDict.__init__(self, _cmp_table)

        # Go ahead and compile it
        self._compile()

    def _compile(self): 
        """ Builds a regular expression object based on the keys of the
        dictionary """

        keys = self.keys()
        tmp = "(%s)" % "|".join(map(re.escape, keys))
        self.re = tmp
        self.regex = re.compile(self.re)
    
    def __call__(self, mo): 
        """ Handler for each regex match """
        matchstr = mo.string[mo.start():mo.end()]
        return self[matchstr]
    
    def Convert(self, text): 
        """ Translates and returns the modified text """ 
        return self.regex.sub(self, string.lower(text))

#
# Test routine
#

if __name__ == "__main__":
    """ Read user input and output Unicode polytonic greek """
    conv = Convertor()
    norm = Normalizer()
    print "Pseudo-BetaCode demo (enter 'q' to quit)"
    s = ''
    while 1:
        s = raw_input("> ")
        if s == 'q': break
        print conv.Convert(s)
        print norm.Convert(s)

