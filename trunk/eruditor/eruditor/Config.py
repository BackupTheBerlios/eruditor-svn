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
This module provides an easy way to modify and access configuration settings.
It allows global access from any other part of the program.
"""

import wx
import os.path

config = None

_styles = (wx.NORMAL, wx.SLANT, wx.ITALIC)
_weights = (wx.NORMAL, wx.LIGHT, wx.BOLD)
_min_size = 1
_max_size = 72

TEXT = "text"
LIST = "list"

def Initialize():
    global config
    if config:
        print "ERROR: double initialization"
        return

    config = wx.Config("eruditor")

    # Font settings

    for type in [TEXT, LIST]:
        face = config.Read("/%sfont/face"%type, defaultVal="Times New Roman")
        style = config.ReadInt("/%sfont/style"%type, defaultVal=wx.NORMAL)
        weight = config.ReadInt("/%sfont/weight"%type, defaultVal=wx.NORMAL)
        size = config.ReadInt("/%sfont/size"%type, defaultVal=12)

        if not (style and style in _styles): style = wx.NORMAL
        if not (weight and weight in _weights): weight = wx.NORMAL
        if not (size >= _min_size and size <= _max_size): size = 12

        config.Write("/%sfont/face"%type, face)
        config.WriteInt("/%sfont/style"%type, style)
        config.WriteInt("/%sfont/weight"%type, weight)
        config.WriteInt("/%sfont/size"%type, size)

    config.Flush()

def _SetFont(type, face, style, weight, size):
    assert style in _styles
    assert weight in _weights
    assert size >= _min_size and size <= _max_size

    config.Write("/%sfont/face"%type, face)
    config.WriteInt("/%sfont/style"%type, style)
    config.WriteInt("/%sfont/weight"%type, weight)
    config.WriteInt("/%sfont/size"%type, size)

def _GetFont(type):
    font = wx.Font(
            config.ReadInt("/%sfont/size"%type),
            wx.TELETYPE,
            config.ReadInt("/%sfont/style"%type),
            config.ReadInt("/%sfont/weight"%type),
            False,
            config.Read("/%sfont/face"%type))
    return font

def SetTextFont(face, style, weight,size):
    _SetFont(TEXT, face, style, weight, size)

def GetTextFont():
    return _GetFont(TEXT)

def SetListFont(face, style, weight,size):
    _SetFont(LIST, face, style, weight, size)

def GetListFont():
    return _GetFont(LIST)

def SetLastDir(dir):
    if os.path.exists(dir):
        dir = os.path.abspath(dir)
        config.Write("/file/lastdir", dir)

def GetLastDir():
    dir = config.Read("/file/lastdir", defaultVal=".")

    if os.path.exists(dir):
        return dir
    else:
        config.Write("/file/lastdir", ".")
        return "."

