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
# File: Globals.py
# Author: Alexander Lee
#
# Ghetto substitute for a config file.

import datetime
import Types

# Main

APPNAME = u"ērudītor"

# Lesson

DEFAULT_TITLE = "Unnamed Lesson"
DEFAULT_TYPE = Types.DefaultType()

TIMES = [ 1, 2, 3, 5, 8 ]
""" The number of days to wait before expiring cards in each long-term pile
(i.e. cards of each count level). Beyond this, I don't know what happens. """

TIME_DELTAS = [ datetime.timedelta(x) for x in TIMES ]
""" The corresponding time deltas """

# Card stacks

SUMMARY = "Summary"
UNLEARNED = "Unlearned"
ULTRASHORT = "Ultrashort"
SHORTTERM = "Shortterm"

LEARNED = [ "Learned%i" % x for x in range(len(TIMES)) ]
STACKNAMES = [SUMMARY, UNLEARNED, ULTRASHORT, SHORTTERM] + LEARNED

# Card

FRONT, MIDDLE, BACK = 0, 1, 2
SIDENAMES = {
    FRONT:  "headwords",
    MIDDLE: "extra info",
    BACK:   "definitions",
}


