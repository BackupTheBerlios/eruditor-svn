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
Custom wx.ListCtrl that handles the summary display of cards in the main
window.
"""

import sys
import wx

import Config
import EditDialog

from Globals import *

class CardList(wx.ListCtrl):
    """ The custom list control """

    def __init__(self, parent, ID):
        wx.ListCtrl.__init__(self, parent, ID,
                style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.SUNKEN_BORDER)

        # Set up columns

        self.InsertColumn(0, u"§")
        self.InsertColumn(1, "front")
        self.InsertColumn(2, "middle")
        self.InsertColumn(3, "back")
        self.InsertColumn(4, "learned")
        self.InsertColumn(5, "n")

        self.SetColumnWidth(0, 20)
        self.SetColumnWidth(1, 150)
        self.SetColumnWidth(2, 150)
        self.SetColumnWidth(3, 150)
        self.SetColumnWidth(4, 130)
        self.SetColumnWidth(5, 20)

        # Private fields and basic initialization

        self.__lesson = None
        """ The lesson to display """
        self.__stackname = None
        """ Name of stack whose cards will be displayed """
        self.__stack = None
        """ Quick reference to that stack """
        self.SetItemCount(0)

        # Row attributes -- for fonts and colors

        red    = wx.Colour(255, 191, 191)
        green  = wx.Colour(191, 255, 191)
        blue   = wx.Colour(191, 191, 255)

        self.__unl_attr = wx.ListItemAttr()
        """ Row attribute for unlearned cards """
        self.__lrn_attr = wx.ListItemAttr()
        """ Row attribute for learned cards """
        self.__exp_attr = wx.ListItemAttr()
        """ Row attribute for expired cards """

        # These are the default colors for the three types
        self.__unl_attr.SetBackgroundColour(red)
        self.__lrn_attr.SetBackgroundColour(green)
        self.__exp_attr.SetBackgroundColour(blue)

        self.SetFont(Config.GetListFont())

        # Events

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnActivate, self)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self)

    def SetFont(self, font):
        """ Sets the font for the headings and rows """
        wx.ListCtrl.SetFont(self, font)
        self.__unl_attr.SetFont(font)
        self.__lrn_attr.SetFont(font)
        self.__exp_attr.SetFont(font)

    def OnGetItemText(self, item, col):
        """ Callback for showing list contents """
        card = self.__stack[item]
        if col == 0: return card.section
        elif col <= 3: return card.GetText(col-1) # FIXME hackish ... ?
        elif col == 4: return card.GetLearnedPretty(self.__lesson.focus)
        elif col == 5: return card.GetCountStr(self.__lesson.focus)
        assert False

    def OnGetItemAttr(self, item):
        """ Callback for showing list contents """
        card = self.__stack[item]
        if card.GetCount(self.__lesson.focus) == 0: return self.__unl_attr
        elif card.IsExpired(self.__lesson.focus): return self.__exp_attr
        else: return self.__lrn_attr

    def GetSelectedCards(self):
        cards = []
        idx = self.GetFirstSelected()
        while idx != -1:
            c = self.__stack[idx]
            #print c
            cards.append(c)
            # Unselect it
            self.SetItemState(idx, 0, wx.LIST_STATE_SELECTED)
            # Get next
            idx = self.GetNextSelected(idx)
        return cards

    # Property: stackname
    def SetStackName(self, stackname):
        """ Sets the associated stack as the list's data source """
        self.__stackname = stackname
        self.__stack = self.__lesson.stacks[stackname]
        self.SetItemCount(len(self.__stack))
    def GetStackName(self):
        return self.__stackname
    stackname = property(GetStackName, SetStackName)

    # Property: lesson
    def SetLesson(self, lesson):
        self.__lesson = lesson
    def GetLesson(self):
        return self.__lesson
    lesson = property(GetLesson, SetLesson)

    def OnActivate(self, event):
        """ Handler for double-click or enter """
        idx = event.GetIndex() #event.m_itemIndex
        card = self.__stack[idx]

        dlg = EditDialog.EditDialog(self, card=card)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnColClick(self, event):
        """ Handler for column sort (user click on header) """
        col = event.GetColumn() #event.m_col
        if col == 0: self.__lesson.SortBySection()
        elif col == 1: self.__lesson.SortByFront()
        elif col == 2: self.__lesson.SortByMiddle()
        elif col == 3: self.__lesson.SortByBack()
        elif col == 4: self.__lesson.SortByLearned()
        elif col == 5: self.__lesson.SortByCount()
        self.Refresh()

