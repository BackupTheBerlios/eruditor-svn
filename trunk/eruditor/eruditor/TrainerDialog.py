# -*- coding: UTF-8 -*-
# generated by wxGlade 0.3.5.1 on Fri Mar 25 18:49:33 2005
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

import datetime

import Config
import EditDialog

from Globals import *

TICK = 1000
SHOWSEC = 18 # sec
TESTMIN = 12 # min

_second = datetime.timedelta(seconds=1)
_zero = datetime.timedelta()

# begin wxGlade: dependencies
# end wxGlade

class TrainerDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TrainerDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.labelMessage = wx.StaticText(self, -1, "MESSAGE")
        self.textFront = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.textMiddle = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.textBack = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.labelTimerShow = wx.StaticText(self, -1, "seconds", style=wx.ST_NO_AUTORESIZE)
        self.labelTimerTest = wx.StaticText(self, -1, "minutes", style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        self.buttonEdit = wx.BitmapButton(self, wx.NewId(), wx.Bitmap("img/edit.png", wx.BITMAP_TYPE_ANY))
        self.buttonExit = wx.BitmapButton(self, wx.NewId(), wx.Bitmap("img/exit.png", wx.BITMAP_TYPE_ANY))
        self.buttonNext = wx.Button(self, wx.NewId(), "N&ext Card")
        self.buttonYes = wx.BitmapButton(self, -1, wx.Bitmap("img/accept.png", wx.BITMAP_TYPE_ANY))
        self.buttonNo = wx.BitmapButton(self, -1, wx.Bitmap("img/cancel.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        font = Config.GetTextFont()
        self.textFront.SetFont(font)
        self.textMiddle.SetFont(font)
        self.textBack.SetFont(font)

        self.curr = None

    def __set_properties(self):
        # begin wxGlade: TrainerDialog.__set_properties
        self.SetTitle("Card Trainer")
        self.labelMessage.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.textFront.SetSize((300,60))
        self.textMiddle.SetSize((300, 60))
        self.textBack.SetSize((300,60))
        self.labelTimerShow.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelTimerShow.SetToolTipString("Timer for ultra-shortterm memory")
        self.labelTimerTest.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelTimerTest.SetToolTipString("Timer for shortterm memory")
        self.buttonEdit.SetSize(self.buttonEdit.GetBestSize())
        self.buttonExit.SetSize(self.buttonExit.GetBestSize())
        self.buttonNext.SetFocus()
        self.buttonYes.Enable(False)
        self.buttonYes.SetSize(self.buttonYes.GetBestSize())
        self.buttonNo.Enable(False)
        self.buttonNo.SetSize(self.buttonNo.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: TrainerDialog.__do_layout
        sizerCardTrainer = wx.BoxSizer(wx.VERTICAL)
        sizerButtons = wx.BoxSizer(wx.HORIZONTAL)
        sizerTimer = wx.BoxSizer(wx.HORIZONTAL)
        sizerCardTrainer.Add(self.labelMessage, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5)
        sizerCardTrainer.Add(self.textFront, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5)
        sizerCardTrainer.Add(self.textMiddle, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5)
        sizerCardTrainer.Add(self.textBack, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5)
        sizerTimer.Add(self.labelTimerShow, 1, wx.EXPAND|wx.FIXED_MINSIZE, 5)
        sizerTimer.Add(self.labelTimerTest, 1, wx.EXPAND|wx.FIXED_MINSIZE, 5)
        sizerCardTrainer.Add(sizerTimer, 0, wx.ALL|wx.EXPAND, 5)
        sizerButtons.Add(self.buttonEdit, 0, wx.RIGHT|wx.FIXED_MINSIZE, 5)
        sizerButtons.Add(self.buttonExit, 0, wx.FIXED_MINSIZE, 5)
        sizerButtons.Add((20, 20), 1, wx.FIXED_MINSIZE, 0)
        sizerButtons.Add(self.buttonNext, 0, wx.RIGHT|wx.EXPAND, 5)
        sizerButtons.Add(self.buttonYes, 0, wx.LEFT|wx.RIGHT|wx.FIXED_MINSIZE, 5)
        sizerButtons.Add(self.buttonNo, 0, wx.FIXED_MINSIZE, 5)
        sizerCardTrainer.Add(sizerButtons, 0, wx.ALL|wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(sizerCardTrainer)
        sizerCardTrainer.Fit(self)
        sizerCardTrainer.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def OnButtonEdit(self, event):
        """ TODO unimplmented """
        if self.curr:
            dlg = EditDialog.EditDialog(self, card=self.curr)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def OnButtonExit(self, event):
        self.Close()


# end of class TrainerDialog

class TrainerLearnDialog(TrainerDialog):
    """ Version of the TrainerDialog that handles learning of new cards """

    def __init__(self, *args, **kwds):
        # Get a custom arg and remove from kwds dict.
        # FIXME see PropertiesDialog.py
        self.lesson = kwds["lesson"]
        del kwds["lesson"]
        self.parent = args[0]

        # Call parent constructor
        TrainerDialog.__init__(self, *args, **kwds)

        # Set up timers
        self.showtime = SHOWSEC
        self.testtime = datetime.timedelta(minutes=TESTMIN)

        self._RefreshShowTimer()
        self._RefreshTestTimer()

        self.showtimer = wx.PyTimer(self.NotifyShow)
        """ Timer for ultrashort card-showing """
        self.testtimer = wx.PyTimer(self.NotifyTest)
        """ Timer for shortterm card-testing """

        # Events
        self.Bind(wx.EVT_CLOSE, self.OnWindowClose)
        self.Bind(wx.EVT_BUTTON, self.OnButtonEdit, self.buttonEdit)
        self.Bind(wx.EVT_BUTTON, self.OnButtonExit, self.buttonExit)
        self.Bind(wx.EVT_BUTTON, self.OnButtonNext, self.buttonNext)
        self.Bind(wx.EVT_BUTTON, self.OnButtonYes, self.buttonYes)
        self.Bind(wx.EVT_BUTTON, self.OnButtonNo, self.buttonNo)

        # Begin the process
        self.process = self.Process()
        self.process.next()
        self.parent.pilesPanel.Update(self.parent.lesson)

    def OnWindowClose(self, event):
        result = wx.MessageBox(
            "Cancel training?", "Confirm",
            wx.YES_NO|wx.CENTRE|wx.ICON_QUESTION)
        if result == wx.YES:
            self.showtimer.Stop()
            self.testtimer.Stop()
            del self.process
            event.Skip() # Let the window close

    def OnButtonNext(self, event):
        """ Handles clicks on the main button """
        try:
            self.process.next()
            self.parent.pilesPanel.Update(self.parent.lesson)
        except StopIteration:
            # But this should never happen...
            print "ERR process ended (How'd I get here?)"
            raise

    def OnButtonYes(self, event):
        self.gotit = True
        self.process.next()
        self.parent.pilesPanel.Update(self.parent.lesson)

    def OnButtonNo(self, event):
        self.gotit = False
        self.process.next()
        self.parent.pilesPanel.Update(self.parent.lesson)

    def Process(self):
        """ Handles all training logic.
        This is implemented as a generator. Generators are awesome. """

        # The stacks we're working with:
        unlearned = self.lesson.stacks[UNLEARNED]
        ultrashort = self.lesson.stacks[ULTRASHORT]
        shortterm = self.lesson.stacks[SHORTTERM]
        learned0 = self.lesson.stacks[LEARNED[0]]

        # Initialization
        self.labelMessage.SetLabel("Try to learn these cards")
        self.buttonNext.SetLabel("B&egin")
        self.buttonNext.SetDefault()
        self._SetButtonsNext()
        yield None

        # Start timers, change label
        self.showtimer.Start(TICK)
        self.testtimer.Start(TICK)
        self.buttonNext.SetLabel("N&ext")

        # Start displaying new cards
        while True:
            # LOOP A
            #print "LOOP A"

            # Show a new card
            card = unlearned[0]
            self._ShowCard(card)
            yield None

            # Move from unlearned to ultrashort
            ultrashort.append(card)
            unlearned.pop(0)

            # Now check for three conditions:
            # 1. no new cards
            # 2. 'showtime' timer ran out
            # 3. 'testtime' timer ran out

            if not unlearned or self.showtime <= 0:
                # TEST B
                #print "TEST B"

                # No new cards or show timer ran out.
                # Start testing the cards that were shown.

                # Begin with a message (but leave timer running)
                self._ClearFields()
                self.labelMessage.SetLabel("Try to remember these cards")
                self.buttonNext.SetLabel("B&egin")
                yield None

                # Loop to give a dialog if there is spare time
                while True:
                    if self.showtime > 0:
                        rval = wx.MessageBox(
                            "The ultra-shortterm timer is still running.\n"+\
                            "Are you sure you want to proceed?", "Proceed?",
                            wx.YES_NO|wx.CENTRE|wx.ICON_QUESTION)
                        if rval == wx.YES:
                            break # Go on
                        else:
                            yield None # Keep waiting
                    else:
                        break # Go on

                # Now stop timer
                self.showtimer.Stop()
                self.showtime = 0
                self._RefreshShowTimer()
                self.buttonNext.SetLabel("N&ext")

                # And show part of the first card
                card = ultrashort[0]
                self._ShowCardAsk(card)
                self.buttonNext.SetLabel("R&eveal")
                yield None

                while True:
                    # LOOP C
                    #print "LOOP C"

                    # Reveal entire card, configure buttons
                    self._ShowCard(card)
                    self._SetButtonsYesNo()
                    yield None

                    # Check answer, move card to proper stack
                    if self.gotit: shortterm.append(card)
                    else: unlearned.insert(0, card)
                    ultrashort.pop(0)
                    self._SetButtonsNext()

                    # Now check for more conditions:
                    if self.testtime <= _zero:
                        # Test timer ran out.
                        self._ClearFields()
                        break 
                        # Now go down (TEST D)

                    elif unlearned and not ultrashort:
                        # Ran out of cards, jump out of loop
                        # and go back to showing new cards (LOOP A)

                        self._ClearFields()
                        self.labelMessage.SetLabel("Try to learn these cards")
                        self.buttonNext.SetLabel("B&egin")
                        yield None

                        self.showtime = SHOWSEC
                        self.showtimer.Start(TICK)
                        self._RefreshShowTimer()
                        self.buttonNext.SetLabel("N&ext")

                        break 
                        # Now go back up (LOOP A)

                    elif not unlearned and not ultrashort:
                        self._ClearFields()
                        break
                        # Now go down (TEST D)

                    # Show next card
                    card = ultrashort[0]
                    self._ShowCardAsk(card)
                    yield None

                    # Now go back up (LOOP C)

            if not unlearned or self.testtime <= _zero:
                # TEST D
                #print "TEST D"

                # Ok, either we're through all the new cards, or the test timer
                # has run out. Now we're gonna test the cards in the
                # "shortterm stack", and hopefully move them to "learned0"!

                self.labelMessage.SetLabel("Testing cards in your shortterm memory")
                self.buttonNext.SetLabel("B&egin")
                self.buttonNext.SetDefault()
                self.buttonNext.SetFocus()
                yield None

                # Loop to give a dialog if there is spare time
                while True:
                    if self.testtime > _zero:
                        rval = wx.MessageBox(
                            "The shortterm timer is still running.\n"+\
                            "Are you sure you want to proceed?", "Proceed?",
                            wx.YES_NO|wx.CENTRE|wx.ICON_QUESTION)
                        if rval == wx.YES:
                            break # Go on
                        else:
                            yield None # Keep waiting
                    else:
                        break # Go on

                # Reset the timer
                self.testtimer.Stop()
                self.testtime = _zero
                self._RefreshTestTimer()
                self.buttonNext.SetLabel("N&ext")

                # And show part of the first card
                card = shortterm[0]
                self._ShowCardAsk(card)
                self.buttonNext.SetLabel("R&eveal")
                yield None

                while True:
                    # LOOP E
                    #print "LOOP E"

                    # Reveal entire card, configure buttons
                    self._ShowCard(card)
                    self._SetButtonsYesNo()
                    yield None

                    # Check answer, move card to proper stack
                    if self.gotit:
                        # Learned it!
                        card.Upgrade(self.lesson.focus)
                        learned0.append(card)
                        self.lesson.dirty = True
                    else: unlearned.insert(0, card)
                    shortterm.pop(0)
                    self._SetButtonsNext()

                    if not shortterm:
                        # Ran out of cards, we're done!
                        #print "DONE"
                        self._ClearFields()
                        self.buttonNext.Enable(False)
                        self.labelMessage.SetLabel("Sesson finished!")
                        self.buttonExit.SetFocus()
                        yield None
                        return

                    # Show part of the next card
                    card = shortterm[0]
                    self._ShowCardAsk(card)
                    yield None

                    # Back up to next card (LOOP E)

    def _ShowCard(self, card):
        """ Shows all sides of the given card """
        self.textFront.SetValue(card.GetText(FRONT))
        self.textMiddle.SetValue(card.GetText(MIDDLE))
        self.textBack.SetValue(card.GetText(BACK))
        self.curr = card

    def _ShowCardAsk(self, card):
        """ Shows all sides except the one being studied """
        if self.lesson.focus == FRONT:
            self.textFront.SetValue("")
            self.textMiddle.SetValue(card.GetText(MIDDLE))
            self.textBack.SetValue(card.GetText(BACK))
        elif self.lesson.focus == MIDDLE:
            self.textFront.SetValue(card.GetText(FRONT))
            self.textMiddle.SetValue("")
            self.textBack.SetValue(card.GetText(BACK))
        elif self.lesson.focus == BACK:
            self.textFront.SetValue(card.GetText(FRONT))
            self.textMiddle.SetValue(card.GetText(MIDDLE))
            self.textBack.SetValue("")
        self.curr = card

    def _ClearFields(self):
        """ Clears out the three text fields """
        self.textFront.SetValue("")
        self.textMiddle.SetValue("")
        self.textBack.SetValue("")
        self.curr = None

    def _SetButtonsYesNo(self):
        """ Disables 'next' button, enables 'yes' and 'no' """
        self.buttonNext.Enable(False)
        self.buttonYes.Enable(True)
        self.buttonNo.Enable(True)
        self.buttonYes.SetFocus()

    def _SetButtonsNext(self):
        """ Enables 'next' button, disables 'yes' and 'no' """
        self.buttonNext.Enable(True)
        self.buttonYes.Enable(False)
        self.buttonNo.Enable(False)
        self.buttonNext.SetFocus()

    def NotifyShow(self):
        """ Callback for the ultrashort timer """
        self.showtime -= 1
        if self.showtime == 0: # time ran out
            self.showtimer.Stop()
        self._RefreshShowTimer()

    def NotifyTest(self):
        """ Callback for the shortterm timer """
        self.testtime -= _second
        if self.testtime == _zero:
            self.testtimer.Stop()
        self._RefreshTestTimer()

    def _RefreshShowTimer(self):
        self.labelTimerShow.SetLabel("%s seconds" % str(self.showtime))

    def _RefreshTestTimer(self):
        self.labelTimerTest.SetLabel("%s minutes" % str(self.testtime))

class TrainerReviewDialog(TrainerDialog):
    """ Version of the TrainerDialog that handles testing of expired cards to
    see if student has remembered them """

    def __init__(self, *args, **kwds):
        # Get a custom arg and remove from kwds dict.
        # FIXME see PropertiesDialog.py
        self.lesson = kwds["lesson"]
        del kwds["lesson"]
        self.parent = args[0]

        # Call parent constructor
        TrainerDialog.__init__(self, *args, **kwds)

        # Events
        self.Bind(wx.EVT_CLOSE, self.OnWindowClose)
        self.Bind(wx.EVT_BUTTON, self.OnButtonEdit, self.buttonEdit)
        self.Bind(wx.EVT_BUTTON, self.OnButtonExit, self.buttonExit)
        self.Bind(wx.EVT_BUTTON, self.OnButtonNext, self.buttonNext)
        self.Bind(wx.EVT_BUTTON, self.OnButtonYes, self.buttonYes)
        self.Bind(wx.EVT_BUTTON, self.OnButtonNo, self.buttonNo)

        # Clear the labels -- we don't need them
        self.labelTimerShow.SetLabel("")
        self.labelTimerTest.SetLabel("")

        # Begin the process
        self.process = self.Process()
        self.process.next()
        self.parent.pilesPanel.Update(self.parent.lesson)

    def OnWindowClose(self, event):
        result = wx.MessageBox(
            "Cancel training?", "Confirm",
            wx.YES_NO|wx.CENTRE|wx.ICON_QUESTION)
        if result == wx.YES:
            del self.process
            event.Skip() # Let the window close

    def OnButtonNext(self, event):
        """ Handles clicks on the main button """
        try:
            self.process.next()
            self.parent.pilesPanel.Update(self.parent.lesson)
        except StopIteration:
            # But this should never happen...
            print "ERR process ended (How'd I get here?)"
            raise

    def OnButtonYes(self, event):
        self.gotit = True
        self.process.next()
        self.parent.pilesPanel.Update(self.parent.lesson)

    def OnButtonNo(self, event):
        self.gotit = False
        self.process.next()
        self.parent.pilesPanel.Update(self.parent.lesson)

    def Process(self):
        """ Handles all training logic.
        This is implemented as a generator. Generators are awesome. """

        # The stacks we're working with:
        expired = self.lesson.GetExpiredCards()
        unlearned = self.lesson.stacks[UNLEARNED]

        # Initialization
        self.labelMessage.SetLabel("See if you remember these cards")
        self.buttonNext.SetLabel("B&egin")
        self.buttonNext.SetDefault()
        self._SetButtonsNext()
        yield None

        # And show part of the first card
        card = expired[0]
        self._ShowCardAsk(card)
        self.buttonNext.SetLabel("R&eveal")
        yield None

        while True:
            # LOOP A
            #print "LOOP A"

            # Reveal entire card, configure buttons
            self._ShowCard(card)
            self._SetButtonsYesNo()
            yield None

            # Check answer, move card to proper stack
            count = card.GetCount(self.lesson.focus) # get current count
            if self.gotit:
                # Learned it!
                card.Upgrade(self.lesson.focus)
                self.lesson.stacks[LEARNED[count + 1 - 1]].append(card)
            else:
                # Dang, forgot it already...
                card.Downgrade(self.lesson.focus)
                unlearned.insert(0, card)
            expired.pop(0)
            self.lesson.stacks[LEARNED[count - 1]].remove(card)
            self.lesson.dirty = True
            self._SetButtonsNext()

            if not expired:
                # Ran out of cards, we're done!
                #print "DONE"
                self._ClearFields()
                self.buttonNext.Enable(False)
                self.labelMessage.SetLabel("Sesson finished!")
                self.buttonExit.SetFocus()
                yield None
                return

            # Show part of the next card
            card = expired[0]
            self._ShowCardAsk(card)
            yield None

            # Back up to next card (LOOP A)

    def _ShowCard(self, card):
        """ Shows all sides of the given card """
        self.textFront.SetValue(card.GetText(FRONT))
        self.textMiddle.SetValue(card.GetText(MIDDLE))
        self.textBack.SetValue(card.GetText(BACK))
        self.curr = card

    def _ShowCardAsk(self, card):
        """ Shows all sides except the one being studied """
        if self.lesson.focus == FRONT:
            self.textFront.SetValue("")
            self.textMiddle.SetValue(card.GetText(MIDDLE))
            self.textBack.SetValue(card.GetText(BACK))
        elif self.lesson.focus == MIDDLE:
            self.textFront.SetValue(card.GetText(FRONT))
            self.textMiddle.SetValue("")
            self.textBack.SetValue(card.GetText(BACK))
        elif self.lesson.focus == BACK:
            self.textFront.SetValue(card.GetText(FRONT))
            self.textMiddle.SetValue(card.GetText(MIDDLE))
            self.textBack.SetValue("")
        self.curr = card

    def _ClearFields(self):
        """ Clears out the three text fields """
        self.textFront.SetValue("")
        self.textMiddle.SetValue("")
        self.textBack.SetValue("")
        self.curr = None

    def _SetButtonsYesNo(self):
        """ Disables 'next' button, enables 'yes' and 'no' """
        self.buttonNext.Enable(False)
        self.buttonYes.Enable(True)
        self.buttonNo.Enable(True)
        self.buttonYes.SetFocus()

    def _SetButtonsNext(self):
        """ Enables 'next' button, disables 'yes' and 'no' """
        self.buttonNext.Enable(True)
        self.buttonYes.Enable(False)
        self.buttonNo.Enable(False)
        self.buttonNext.SetFocus()

    def NotifyShow(self):
        """ Callback for the ultrashort timer """
        self.showtime -= 1
        if self.showtime == 0: # time ran out
            self.showtimer.Stop()
        self._RefreshShowTimer()

    def NotifyTest(self):
        """ Callback for the shortterm timer """
        self.testtime -= _second
        if self.testtime == _zero:
            self.testtimer.Stop()
        self._RefreshTestTimer()

    def _RefreshShowTimer(self):
        self.labelTimerShow.SetLabel("%s seconds" % str(self.showtime))

    def _RefreshTestTimer(self):
        self.labelTimerTest.SetLabel("%s minutes" % str(self.testtime))

