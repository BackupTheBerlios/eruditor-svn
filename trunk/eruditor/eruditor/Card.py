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
# File: Card.py
# Author: Alexander Lee
#
# Card stuff.
#
# Date storage and formatting done with the help of the 20050216 entry at
# www.kenkinder.com; necessary cause the ``datetime`` module seems to suck.

import datetime

import Types

from Globals import *

class Card(object):
    """ Represents a single flash card. """

    def __init__(self, type, ft, fl, fx, mt, ml, mx, bt, bl, bx, section):
        self.type = type
        """ The type of card (i.e. language) being learned """
        self.section = section
        """ For organization """
        self.update(ft, fl, fx, mt, ml, mx, bt, bl, bx)

    def __repr__(self):
        return "<Card %s>" % self.text[FRONT]

    def update(self, ft, fl, fx, mt, ml, mx, bt, bl, bx):
        """ Set the text, learned-dates, and counts for all sides of the card
        """
        self.text = [ft, mt, bt]
        """ Text contained on each side """
        self.learned = [fl, ml, bl]
        """ When each side was last learned """
        self.count = [fx, mx, bx]
        """ How many times each side was correctly known """
        self.expired = [False, False, False]
        """ Has the card expired? Start with dummy values """

    def SetText(self, side, text):
        assert side in (FRONT, MIDDLE, BACK)
        self.text[side] = text

    def GetText(self, side):
        assert side in (FRONT, MIDDLE, BACK)
        if side == BACK: return self.text[side]
        else: return Types.Convert(self.type, self.text[side])

    def GetTextRaw(self, side):
        assert side in (FRONT, MIDDLE, BACK)
        return self.text[side]

    def Upgrade(self, side):
        """ Upgrades card to next 'learned' level.
        Returns the new learned count. """
        assert side in (FRONT, MIDDLE, BACK)
        self.count[side] += 1
        if self.count[side] > len(LEARNED):
            self.count[side] = len(LEARNED) # maxed out
        self.learned[side] = datetime.datetime.now()
        self.expired[side] = False
        return self.count[side]

    def Downgrade(self, side):
        """ Demotes card all the way to 'unlearned' status """
        assert side in (FRONT, MIDDLE, BACK)
        self.count[side] = 0
        self.learned[side] = None
        self.expired[side] = False

    def GetLearned(self, side):
        assert side in (FRONT, MIDDLE, BACK)
        if self.count[side] == 0: return None
        else:
            dt = self.learned[side]
            return '%s %s %s %s %s %s' % \
                (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    def GetLearnedPretty(self, side):
        assert side in (FRONT, MIDDLE, BACK)
        if self.count[side] == 0: return "Never"
        else: return self.learned[side].strftime("%a, %d %b %Y")

    def GetCount(self, side):
        assert side in (FRONT, MIDDLE, BACK)
        return self.count[side]

    def GetCountStr(self, side):
        assert side in (FRONT, MIDDLE, BACK)
        count = self.count[side]
        if count: return str(count)
        else: return ""

    def Expire(self, side):
        """ Manually expire card """
        if self.count[side] > 0:
            self.expired[side] = True

    def IsExpired(self, side):
        """ Return the cached expired status """
        return self.expired[side]

    def CheckExpired(self, side, date):
        """ See if given side of card has expired on given date.
        The result is cached. If a cached affirmative exists, use that. """
        # First, if already expired, then just return that
        # This helps with (a) optimization (unimportant)
        # And (b) manual expiration (important)
        count = self.count[side]
        if self.expired[side]:
            return True
        # Else, calculate it against supplied date
        else:
            self.expired[side] = \
                ( date - self.learned[side] > TIME_DELTAS[count-1] )
            return self.expired[side]

