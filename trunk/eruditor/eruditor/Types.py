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
# File: Types.py
# Author: Alexander Lee
#
# Module to handle all card types. Each type has an associated Convertor
# class, which handles the text->unicode convertion for that type.

_default = None
""" The name of the default type """
_types = {}
""" Dictionary of types. Maps type name to Convertor class. """

def DefaultType():
    """ Returns the name of the default type """
    return _default

def TypesList():
    """ Returns a string list of type names """
    names = _types.keys()
    names.sort()
    return names

def ValidType(type):
    """ Tell us if a given language is supported """
    return (type in _types)

def GetConvertor(type):
    """ Returns the convertor for the specified type """
    # FIXME is this function even needed?
    try:
        conv = _types[type][0]
        return conv
    except KeyError:
        print "ERR: No such type registered!"
        raise

def Convert(type, text):
    """ Runs conversion of given type on the given text """
    try:
        conv = _types[type][0]
        return conv.Convert(text)
    except KeyError:
        print "ERR: No such type registered!"
        raise

def Normalize(type, text):
    """ Gets a plain cmp()-arable version of the text """
    try:
        norm = _types[type][1]
        return norm.Convert(text)
    except KeyError:
        print "ERR: No such type registered!"
        raise

def RegisterType(typename):
    """ Registers the given type. A "modname".py file must exist, and it must
    contain a Convertor class. """
    try:
        module = __import__(typename)
        conv = module.Convertor()
        norm = module.Normalizer()
        _types[typename] = (conv, norm)
    except ImportError:
        print "ERR: No such type found!"
        raise
    except:
        print "ERR: Could not load the specified type!"
        raise

# Initialization

RegisterType("Plain")
RegisterType("Greek")
RegisterType("Latin")

_default = "Plain"
