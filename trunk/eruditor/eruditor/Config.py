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
# File: Config.py
# Author: Alexander Lee
#
# Module to handle program configuration.

import wx
import os.path

config = None

_styles = (wx.NORMAL, wx.SLANT, wx.ITALIC)
_weights = (wx.NORMAL, wx.LIGHT, wx.BOLD)
_min_size = 1
_max_size = 72

def Initialize():
    global config
    if config:
        print "ERROR: double initialization"
        return

    config = wx.Config("eruditor")

    # Font settings
    face = config.Read("/font/face", defaultVal="Times New Roman")
    style = config.ReadInt("/font/style", defaultVal=wx.NORMAL)
    weight = config.ReadInt("/font/weight", defaultVal=wx.NORMAL)
    size = config.ReadInt("/font/size", defaultVal=12)

    if not (style and style in _styles):
        config.WriteInt("/font/style", wx.NORMAL)
    if not (weight and weight in _weights):
        config.WriteInt("/font/weight", wx.NORMAL)
    if not (size >= _min_size and size <= _max_size):
        config.WriteInt("/font/size", 12)

def SetFont(face, style, weight, size):
    assert style in _styles
    assert weight in _weights
    assert size >= _min_size and size <= _max_size

    config.Write("/font/face", face)
    config.WriteInt("/font/style", style)
    config.WriteInt("/font/weight", weight)
    config.WriteInt("/font/size", size)

def GetFont():
    font = wx.Font(
            config.ReadInt("/font/size"),
            wx.TELETYPE,
            config.ReadInt("/font/style"),
            config.ReadInt("/font/weight"),
            False,
            config.Read("/font/face"))
    return font

def SetLastDir(dir):
    if os.path.exists(dir):
        config.Write("/file/lastdir", dir)

def GetLastDir():
    dir = config.Read("/file/lastdir", defaultVal=".")

    if os.path.exists(dir):
        return dir
    else:
        config.Write("/file/lastdir", ".")
        return "."

