# -*- coding: UTF-8 -*-
# generated by wxGlade 0.3.5.1 on Sat Mar 19 17:39:40 2005
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

import wx

# begin wxGlade: dependencies
# end wxGlade

class AboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.aboutHeader = wx.StaticText(self, -1, "ērudītor")
        self.labelVersion = wx.StaticText(self, -1, "version 1.0")
        self.aboutMessage = wx.StaticText(self, -1, "A vocabulary training program for Classicists.\nSupports Greek, Latin, and generic Unicode.\n\nImplemented in Python, using:\n  - wxPython: http://wxpython.org/\n  - wxGlade: http://wxglade.sourceforge.net/\nInspired by:\n  - Pauker: http://pauker.sourceforge.net/\n\nWritten by Alex Lee <alexlee@uchicago.edu>\nhttp://home.uchicago.edu/~alexlee/eruditor/")
        self.aboutBitmap = wx.StaticBitmap(self, -1, wx.Bitmap("img/gibbon.jpg", wx.BITMAP_TYPE_ANY))
        self.buttonOk = wx.Button(self, wx.ID_OK, "OK")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle("About ērudītor")
        self.SetSize((345, 509))
        self.aboutHeader.SetFont(wx.Font(20, wx.ROMAN, wx.NORMAL, wx.BOLD, 0, ""))
        self.aboutBitmap.SetSize((200, 242))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        aboutSizer = wx.BoxSizer(wx.VERTICAL)
        aboutSizer.Add(self.aboutHeader, 0, wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 5)
        aboutSizer.Add(self.labelVersion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 0)
        aboutSizer.Add(self.aboutMessage, 0, wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 10)
        aboutSizer.Add(self.aboutBitmap, 0, wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 10)
        aboutSizer.Add(self.buttonOk, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 10)
        self.SetAutoLayout(True)
        self.SetSizer(aboutSizer)
        self.Layout()
        # end wxGlade

# end of class AboutDialog

