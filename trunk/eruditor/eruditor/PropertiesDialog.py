# -*- coding: UTF-8 -*-
# generated by wxGlade 0.3.5.1 on Sun Mar 20 13:41:16 2005
#
# File: $Id$
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

import wx

import Types

# begin wxGlade: dependencies
# end wxGlade

class PropertiesDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # Get a custom arg and remove from kwds dict.
        # FIXME this doesn't seem like the best way to do this.
        self.lesson = kwds["lesson"]
        del kwds["lesson"]

        # begin wxGlade: PropertiesDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.propsHeader = wx.StaticText(self, -1, "Lesson Properties")
        self.propsTitle = wx.StaticText(self, -1, "Title:")
        self.textTitle = wx.TextCtrl(self, -1, "")
        self.propsType = wx.StaticText(self, -1, "Card type:")
        self.typeListBox = wx.ListBox(self, -1, choices=[], style=wx.LB_SINGLE)
        self.propsDesc = wx.StaticText(self, -1, "Description:")
        self.textDesc = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.propsNotes = wx.StaticText(self, -1, "Notes:")
        self.textNotes = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.buttonOk = wx.Button(self, wx.ID_OK, "OK")
        self.buttonCancel = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        self._Populate()
        #self.Bind(wx.EVT_BUTTON, self.OnButtonOk, self.buttonOk)
        #self.Bind(wx.EVT_BUTTON, self.OnButtonCancel, self.buttonCancel)
        wx.EVT_BUTTON(self, self.buttonOk.GetId(), self.OnButtonOk)
        wx.EVT_BUTTON(self, self.buttonCancel.GetId(), self.OnButtonCancel)

    def __set_properties(self):
        # begin wxGlade: PropertiesDialog.__set_properties
        self.SetTitle("Lesson Properties")
        self.propsHeader.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.textTitle.SetSize((160, 24))
        self.typeListBox.SetSize((160, 54))
        self.textDesc.SetSize((320, 96))
        self.textNotes.SetSize((320, 96))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PropertiesDialog.__do_layout
        sizerVert = wx.BoxSizer(wx.VERTICAL)
        sizerButtons = wx.BoxSizer(wx.HORIZONTAL)
        sizerGrid = wx.FlexGridSizer(4, 2, 10, 10)
        sizerVert.Add(self.propsHeader, 0, wx.ALL|wx.FIXED_MINSIZE, 10)
        sizerGrid.Add(self.propsTitle, 0, wx.ALL|wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 5)
        sizerGrid.Add(self.textTitle, 0, wx.FIXED_MINSIZE, 0)
        sizerGrid.Add(self.propsType, 0, wx.ALL|wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 5)
        sizerGrid.Add(self.typeListBox, 0, wx.FIXED_MINSIZE, 0)
        sizerGrid.Add(self.propsDesc, 0, wx.ALL|wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 5)
        sizerGrid.Add(self.textDesc, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizerGrid.Add(self.propsNotes, 0, wx.ALL|wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 5)
        sizerGrid.Add(self.textNotes, 0, wx.FIXED_MINSIZE, 0)
        sizerVert.Add(sizerGrid, 1, wx.ALL, 10)
        sizerButtons.Add((20, 20), 1, wx.FIXED_MINSIZE, 0)
        sizerButtons.Add(self.buttonOk, 0, wx.RIGHT|wx.FIXED_MINSIZE, 10)
        sizerButtons.Add(self.buttonCancel, 0, wx.FIXED_MINSIZE, 0)
        sizerVert.Add(sizerButtons, 0, wx.ALL|wx.EXPAND, 10)
        self.SetAutoLayout(True)
        self.SetSizer(sizerVert)
        sizerVert.Fit(self)
        sizerVert.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def _Populate(self):
        """ Fills dialog fields with info about the lesson """
        self.textTitle.SetValue(self.lesson.title)
        self.textDesc.SetValue(self.lesson.desc)
        self.textNotes.SetValue(self.lesson.notes)

        # Fill the list of types
        types = Types.TypesList()
        self.typeListBox.InsertItems(Types.TypesList(), 0)

        # Set the selection for this lesson's type
        for i in range(len(types)):
            if types[i] == self.lesson.type:
                self.typeListBox.SetSelection(i)

    def OnButtonOk(self, event):
        """ Takes info from the dialog fields and applies them to the lesson.
        """
        self.lesson.title = self.textTitle.GetValue()
        self.lesson.type = self.typeListBox.GetStringSelection()
        self.lesson.desc = self.textDesc.GetValue()
        self.lesson.notes = self.textNotes.GetValue()
        self.lesson.dirty = True
        event.Skip() # Let normal handler close the dialog

    def OnButtonCancel(self, event):
        event.Skip() # Let normal handler close the dialog

# end of class PropertiesDialog


