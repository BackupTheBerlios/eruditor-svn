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
This module provides visualization support stacks of cards. This way the user
can quickly see how cards are distributed.

First a note on terminology:
- A *stack* is a list of Card objects
- A *pile* is the visualization of a stack

This module defines the following:

:Classes:
    - `PilesPanel`: Shows all piles.
    - `Pile`: Superclass for your basic pile in the `PilesPanel`.
    - `SummaryPile`: Used to displays any and all cards
    - `UnlearnedPile`: Used for unlearned cards
    - `ShortTermPile`: Used for cards in short-term memory
    - `LearnedPile`: Used for cars that have been learned

This module was written with help from the "Doodle" example at Koders.com (for
graphics routines).
"""

import wx

from Globals import *

MIN_WIDTH = 65
MIN_HEIGHT = 140
TOP_MARGIN = 16
FONT_HEIGHT = 16

class PilesPanel(wx.Panel):
    """ Custom widget for showing the piles and their current states """

    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create the piles (visual elements)
        # Do these individually because they're of different subclasses
        self.piles = {}
        self.piles[SUMMARY]    = SummaryPile(self)
        self.piles[UNLEARNED]  = UnlearnedPile(self)
        self.piles[ULTRASHORT] = UnlearnedPile(self, ULTRASHORT)
        self.piles[SHORTTERM]  = UnlearnedPile(self, SHORTTERM)
        for name in LEARNED:
            self.piles[name] = LearnedPile(self, name)

        # Add each of the piles to the sizer
        for name in STACKNAMES:
            sizer.Add(self.piles[name], \
                    1, wx.EXPAND | wx.ALIGN_BOTTOM | wx.ALL, 2)

        self.SetSizer(sizer)

        # Bind click event to each pile
        for name in STACKNAMES:
            wx.EVT_LEFT_DOWN(self.piles[name], self.OnPileClick)

        self.list = None
        """ List that displays the contents of active pile """

        # Set a default active pile.
        # The active pile is the highlighted one, and its cards are shown in
        # the card list ctrl.
        self.activePile = self.piles[SUMMARY]
        self.activePile.SetActive(True)

    def OnPileClick(self, event):
        self.activePile.SetActive(False) # deactivate old pile
        self.activePile = event.GetEventObject()
        self.activePile.SetActive(True) # and activate the new pile
        self.list.stackname = self.activePile.label
	self.list.Refresh()

    def SetCardList(self, list):
        self.list = list

    def Update(self, lesson):
        """ Have the panel draw the status of the given lesson """
        total = lesson.GetCardTotal()

        for name in STACKNAMES:
            unl, lrn, exp = lesson.Breakdown(name)
            self.piles[name].Update(total, unl, lrn, exp)

        # Freshen the list
        self.list.stackname = self.activePile.label

class Pile(wx.Window):
    """ Represents one of the piles of cards in the lesson """

    red    = wx.Colour(255, 128, 128)
    green  = wx.Colour(128, 255, 128)
    blue   = wx.Colour(128, 128, 255)
    yellow = wx.Colour(255,255,128)
    black  = wx.Colour(0, 0, 0)

    def __init__(self, parent, size=(1,1)):
        wx.Window.__init__(self, parent, -1, size=size, style=wx.CLIP_CHILDREN)
        self.SetSizeHints( MIN_WIDTH, MIN_HEIGHT )

        # Colors, pens, and brushes

        self.bgColour = self.GetBackgroundColour()

        self.bgBrush = wx.Brush(self.bgColour)
        self.bgBrushActive = wx.Brush(self.yellow)

        self.unselectPen = wx.Brush(self.black)
        self.selectPen = wx.Brush(self.yellow)

        self.unlearnedBrush = wx.Brush(self.red)
        self.learnedBrush = wx.Brush(self.green)
        self.expiredBrush = wx.Brush(self.blue)

        self.textPen = wx.Pen(self.black)
        self.textFont = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")
        self.textFontActive = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, "")

        # Dummy init values for card stack
        self.unlearned = 0
        """ Number of unlearned cards in this pile """
        self.learned = 0
        """ Number of learned cards in this pile """
        self.expired = 0
        """ Number of expired cards in this pile """
        self.total = 0
        """ Total number of cards in the lesson """

        # Initialize
        self.active = False
        self.InitBuffer()

        # Mouse events
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)

        # Resize and idle events
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        # Refresh event
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def SetActive(self, active):
        self.active = active
        self._Redraw()

    def OnEnter(self, event):
        self._Redraw(self.bgBrushActive)

    def OnLeave(self, event):
        self._Redraw()

    def OnSize(self, event):
        """ Called when the window is resized """
        self.reInitBuffer = True

    def OnIdle(self, event):
        """ If the size was changed then resize to match """
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):
        """ Called when the window is exposed """
        # Apparently, creating the buffered DC will cause the real wx.PaintDC
        # to be created. When it is deleted, the bitmap will be blitted to the
        # real DC. Or something like that.
        dc = wx.BufferedPaintDC(self, self.buffer)

    def InitBuffer(self):
        """ Initalize the bitmap for buffering the display """
        (self.width, self.height) = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(self.width, self.height)
        self._Redraw()
        self.reInitBuffer = False

    def Update(self, total, unlearned, learned, expired):
        """ Called when this tile needs to be redrawn """
        self.total = total
        self.unlearned = unlearned
        self.learned = learned
        self.expired = expired
        self._Redraw()

    def _Redraw(self, bgBrush=None):
        if not bgBrush: bgBrush = self.bgBrush
        dc = wx.BufferedDC(None, self.buffer)
        if self.active: dc.SetBackground(self.bgBrushActive)
        else: dc.SetBackground(bgBrush)
        dc.Clear()
        self._Draw(dc)
        self.Refresh()

    def _Draw(self, dc):
        """ Must be overridden """
        pass

class SummaryPile(Pile):
    """ Pile showing unlearned, learned, and expired """

    def __init__(self, parent, label="Summary"):
        self.label = label
        Pile.__init__(self, parent)

    def _Draw(self, dc):
        """ Draw the card stack """
        width, height = self.GetClientSize()
        n_cards = self.total
        h_stack = height - TOP_MARGIN
        width -= 4

        # Print label
        dc.SetPen(self.textPen)
        if self.active: dc.SetFont(self.textFontActive)
        else: dc.SetFont(self.textFont)
        dc.DrawText(self.label, 1, 1)

        # Calc stack heights
        if not self.total: return
        h_unl = self.unlearned * h_stack / n_cards
        h_lrn = self.learned * h_stack / n_cards
        h_exp = self.expired * h_stack / n_cards

        # Draw stacks
        top = height - 1 - 2

        if h_unl:
            top -= h_unl - 1
            dc.SetBrush(self.unlearnedBrush)
            dc.DrawRectangle(2, top, width, h_unl)
            if h_unl > FONT_HEIGHT:
                dc.DrawText("%i" % self.unlearned, 4, top + 2)

        if h_lrn:
            top -= h_lrn - 1
            dc.SetBrush(self.learnedBrush)
            dc.DrawRectangle(2, top, width, h_lrn)
            if h_lrn > FONT_HEIGHT:
                dc.DrawText("%i" % self.learned, 4, top + 2)

        if h_exp:
            top -= h_exp - 1
            dc.SetBrush(self.expiredBrush)
            dc.DrawRectangle(2, top, width, h_exp)
            if h_exp > FONT_HEIGHT:
                dc.DrawText("%i" % self.expired, 4, top + 2)

class UnlearnedPile(Pile):
    """ Pile showing only unlearned """

    def __init__(self, parent, label="Unlearned"):
        self.label = label
        Pile.__init__(self, parent)

    def _Draw(self, dc):
        """ Draw the card stack """
        width, height = self.GetClientSize()
        n_cards = self.total
        h_stack = height - TOP_MARGIN
        width -= 4

        # Print label
        dc.SetPen(self.textPen)
        if self.active: dc.SetFont(self.textFontActive)
        else: dc.SetFont(self.textFont)
        dc.DrawText(self.label, 1, 1)

        # Calc stack heights
        if not self.total: return
        h_unl = self.unlearned * h_stack / n_cards

        # Draw stacks
        top = height - 1 - 2

        if h_unl:
            top -= h_unl - 1
            dc.SetBrush(self.unlearnedBrush)
            dc.DrawRectangle(2, top, width, h_unl)
            if h_unl > FONT_HEIGHT:
                dc.DrawText("%i" % self.unlearned, 4, top + 2)

class ShortTermPile(Pile):
    """ Pile showing only learned """

    def __init__(self, parent, label):
        self.label = label
        Pile.__init__(self, parent)

    def _Draw(self, dc):
        """ Draw the card stack """
        width, height = self.GetClientSize()
        n_cards = self.total
        h_stack = height - TOP_MARGIN
        width -= 4

        # Print label
        dc.SetPen(self.textPen)
        if self.active: dc.SetFont(self.textFontActive)
        else: dc.SetFont(self.textFont)
        dc.DrawText(self.label, 1, 1)

        # Calc stack heights
        if not self.total: return
        h_lrn = self.learned * h_stack / n_cards

        # Draw stacks
        top = height - 1 - 2

        if h_lrn:
            top -= h_lrn - 1
            dc.SetBrush(self.learnedBrush)
            dc.DrawRectangle(2, top, width, h_lrn)
            if h_lrn > FONT_HEIGHT:
                dc.DrawText("%i" % self.learned, 4, top + 2)
            
class LearnedPile(Pile):
    """ Pile showing learned, expired """

    def __init__(self, parent, label="Learned"):
        self.label = label
        Pile.__init__(self, parent)

    def _Draw(self, dc):
        """ Draw the card stack """
        width, height = self.GetClientSize()
        n_cards = self.total
        h_stack = height - TOP_MARGIN
        width -= 4

        # Print label
        dc.SetPen(self.textPen)
        if self.active: dc.SetFont(self.textFontActive)
        else: dc.SetFont(self.textFont)
        dc.DrawText(self.label, 1, 1)

        # Calc stack heights
        if not self.total: return
        h_lrn = self.learned * h_stack / n_cards
        h_exp = self.expired * h_stack / n_cards

        # Draw stacks
        top = height - 1 - 2

        if h_lrn:
            top -= h_lrn - 1
            dc.SetBrush(self.learnedBrush)
            dc.DrawRectangle(2, top, width, h_lrn)
            if h_lrn > FONT_HEIGHT:
                dc.DrawText("%i" % self.learned, 4, top + 2)

        if h_exp:
            top -= h_exp - 1
            dc.SetBrush(self.expiredBrush)
            dc.DrawRectangle(2, top, width, h_exp)
            if h_exp > FONT_HEIGHT:
                dc.DrawText("%i" % self.expired, 4, top + 2)

