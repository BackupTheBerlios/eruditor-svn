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
# File: Lesson.py
# Author: Alexander Lee
#
# Lesson stuff.

import os.path
import xml.dom.minidom
import datetime
import random

import Card
import Types

from Globals import *

class Lesson(object):
    """ A user's lesson. """

    def __init__(self, filename=None,
                title=DEFAULT_TITLE, type=DEFAULT_TYPE):
        self.title = title
        """ The title of the lesson """
        self.__type = type
        """ The type of cards in this lesson (i.e. language) """
        self.filename = filename
        """ The filename corresponding to this lesson """
        self.dirty = False
        """ Indicates whether the lesson needs to be saved """
        self.desc = ""
        """ Lesson description """
        self.notes = ""
        """ Lesson notes """
        self.__focus = BACK
        """ Which side we're trying to learn right now """

        # Temporary organizational stacks
        self.stacks = {}
        """ Dict of card stacks """
        for name in STACKNAMES:
            self.stacks[name] = []

        if filename:
            self.ReadXML()
            self.SetFocus(BACK)

    def WriteXML(self):
        """ Generates the XML for this lesson and writes it to the specified
        file """

        doc = xml.dom.minidom.Document()

        # The main node
        lesson = doc.createElement("lesson")
        lesson.setAttribute("eruditor-version", "1.0")
        lesson.setAttribute("card-type", self.__type)
        lesson.setAttribute("title", self.title)
        doc.appendChild(lesson)

        # Lesson description
        desc = doc.createElement("description")
        desctxt = doc.createTextNode(self.desc)
        desc.appendChild(desctxt)
        lesson.appendChild(desc)

        # Lesson notes (for student's use)
        notes = doc.createElement("notes")
        notestxt = doc.createTextNode(self.notes)
        notes.appendChild(notestxt)
        lesson.appendChild(notes)

        # The cards
        cards = doc.createElement("cards")
        self._WriteCardsXML(doc, cards, self.stacks[SUMMARY])
        lesson.appendChild(cards)

        # Print it
        outfile = open(self.filename, 'w')
        outfile.write( doc.toprettyxml(indent="  ", encoding="utf-8") )
        outfile.close()

        # Free it
        doc.unlink()

        self.dirty = False

    def _WriteCardsXML(self, doc, node, cards):
        """ Add the cards in the given card-list to the specified DOM node """
        for c in cards:
            cnode = doc.createElement("card")
            if c.section:
                cnode.setAttribute("section", c.section)

            front = doc.createElement("front")
            count = c.GetCount(FRONT)
            front.setAttribute("count", str(count))
            if count:
                learned = c.GetLearned(FRONT)
                front.setAttribute("learned", learned)
            ftxt = doc.createTextNode(c.GetTextRaw(FRONT))
            front.appendChild(ftxt)
            cnode.appendChild(front)

            middle = doc.createElement("middle")
            count = c.GetCount(MIDDLE)
            middle.setAttribute("count", str(count))
            if count:
                learned = c.GetLearned(MIDDLE)
                middle.setAttribute("learned", learned)
            mtxt = doc.createTextNode(c.GetTextRaw(MIDDLE))
            middle.appendChild(mtxt)
            cnode.appendChild(middle)

            back = doc.createElement("back")
            count = c.GetCount(BACK)
            back.setAttribute("count", str(count))
            if count:
                learned = c.GetLearned(BACK)
                back.setAttribute("learned", learned)
            btxt = doc.createTextNode(c.GetTextRaw(BACK))
            back.appendChild(btxt)
            cnode.appendChild(back)

            node.appendChild(cnode)

    def ReadXML(self):
        """ Reads in a XML file for a Lesson and loads it into this object """

        doc = xml.dom.minidom.parse(self.filename)
        lesson = doc.documentElement
        assert lesson.tagName == "lesson"

        self.__type = lesson.getAttribute("card-type")
        self.title = lesson.getAttribute("title")

        desc = lesson.getElementsByTagName("description")
        assert len(desc) == 1
        self.desc = desc[0].childNodes[0].nodeValue.strip()

        notes = lesson.getElementsByTagName("notes")
        assert len(notes) == 1
        self.notes = notes[0].childNodes[0].nodeValue.strip()

        cards = lesson.getElementsByTagName("cards")
        assert len(cards) == 1
        del self.stacks[SUMMARY][:]
        self._ReadCardsXML(cards[0], self.stacks[SUMMARY])

        self.dirty = False

    def _ReadCardsXML(self, src, dest):
        """ Read any cards from the XML node ``src`` and put them into the
        list ``dest`` """

        cards = src.getElementsByTagName("card")
        for c in cards:
            # Section, if any
            section = c.getAttribute("section")

            # Front of card
            fnode = c.getElementsByTagName("front")[0]
            ft = fnode.childNodes[0].nodeValue.strip()
            fx = int(fnode.getAttribute("count"))
            if fx:
                fl = datetime.datetime(
                        *map(int, fnode.getAttribute("learned").split()) )
            else:
                fl = None

            # Middle of card
            mnode = c.getElementsByTagName("middle")[0]
            mt = mnode.childNodes[0].nodeValue.strip()
            mx = int(mnode.getAttribute("count"))
            if mx:
                ml = datetime.datetime(
                        *map(int, mnode.getAttribute("learned").split()) )
            else:
                ml = None

            # Back of card
            bnode = c.getElementsByTagName("back")[0]
            bt = bnode.childNodes[0].nodeValue.strip()
            bx = int(bnode.getAttribute("count"))
            if bx:
                bl = datetime.datetime(
                        *map(int, bnode.getAttribute("learned").split()) )
            else:
                bl = None

            dest.append( Card.Card(self.__type,
                    ft, fl, fx, mt, ml, mx, bt, bl, bx, section) )

    # Property: type
    def SetType(self, type):
        if self.__type != type:
            self.__type = type
            for c in self.stacks[SUMMARY]:
                c.type = type
            self.dirty = True
    def GetType(self):
        return self.__type
    type = property(GetType, SetType)

    # Property: focus
    def SetFocus(self, focus):
        assert focus in (FRONT, MIDDLE, BACK)
        self.__focus = focus
        self.AnalyzeCards()
    def GetFocus(self):
        return self.__focus
    focus = property(GetFocus, SetFocus)
    """ Which side of the cards we are studying """

    def GetBaseName(self):
        if self.filename: return os.path.basename(self.filename)
        else: return "Untitled"

    def GetDirName(self):
        if self.filename: return os.path.dirname(self.filename)
        else: return ""

    def GetCardTotal(self):
        return len(self.stacks[SUMMARY])

    def HasUnlearnedCards(self):
        if self.stacks[UNLEARNED]: return True
        else: return False

    def HasExpiredCards(self):
        for c in self.stacks[SUMMARY]:
            if c.IsExpired(self.focus): return True
        return False

    def GetExpiredCards(self):
        cards = []
        for c in self.stacks[SUMMARY]:
            if c.IsExpired(self.focus): cards.append(c)
        return cards

    def AddCard(self, card, analyze=True):
        # FIXME don't do a full analysis, which is O(n); rather, do an in-place
        # analysis here
        self.stacks[SUMMARY].append(card)
        if analyze: self.AnalyzeCards()
        self.dirty = True

    def DelCard(self, card, analyze=True):
        # FIXME see AddCard
        self.stacks[SUMMARY].remove(card)
        if analyze: self.AnalyzeCards()
        self.dirty = True

    def AnalyzeCards(self):
        """ Copies card references into the various lists, based on their
        status (learned, count). Determines what cards have expired. """

        maxcount = len(TIMES)

        # Clear the stacks!
        for name in STACKNAMES[1:]: # leave out SUMMARY
            del self.stacks[name][:] # clear all others

        # Add references to various stacks.
        # And check for expiration while you're at it!
        for c in self.stacks[SUMMARY]:
            count = c.GetCount(self.__focus)
            if count == 0:
                self.stacks[UNLEARNED].append(c)
            else:
                if count > maxcount:
                    count = maxcount
                    # FIXME use dialog instead!
                    print "INFO Demoted card '%s' to level %i" % \
                            (c.GetText(FRONT), maxcount)
                self.stacks[LEARNED[count - 1]].append(c)

    def Breakdown(self, stackname):
        """ Do a breakdown of the given stack """
        stack = self.stacks[stackname]
        now = datetime.datetime.now()
        unl, lrn, exp = 0, 0, 0

        for c in stack:
            if c.GetCount(self.__focus) == 0:
                unl += 1
            elif c.CheckExpired(self.__focus, now):
                exp += 1
            else:
                lrn += 1

        return unl, lrn, exp

    def ShuffleCards(self):
        """ Randomizes the stack of cards """
        random.shuffle(self.stacks[SUMMARY])
        self.AnalyzeCards()
        self.dirty = True

    def SortBySection(self):
        self.stacks[SUMMARY].sort(self._cmp_section)
        self.AnalyzeCards()
        self.dirty = True

    def SortByFront(self):
        self.stacks[SUMMARY].sort(self._cmp_front)
        self.AnalyzeCards()
        self.dirty = True

    def SortByMiddle(self):
        self.stacks[SUMMARY].sort(self._cmp_middle)
        self.AnalyzeCards()
        self.dirty = True

    def SortByBack(self):
        self.stacks[SUMMARY].sort(self._cmp_back)
        self.AnalyzeCards()
        self.dirty = True

    def SortByLearned(self):
        self.stacks[SUMMARY].sort(self._cmp_learned)
        self.AnalyzeCards()
        self.dirty = True

    def SortByCount(self):
        self.stacks[SUMMARY].sort(self._cmp_count)
        self.AnalyzeCards()
        self.dirty = True

    def _cmp_section(self, c1, c2):
        return cmp(c1.section, c2.section)

    def _cmp_front(self, c1, c2):
        return cmp(c1.GetTextRaw(FRONT), c2.GetTextRaw(FRONT))

    def _cmp_middle(self, c1, c2):
        return cmp(c1.GetTextRaw(MIDDLE), c2.GetTextRaw(MIDDLE))

    def _cmp_back(self, c1, c2):
        return cmp(c1.GetTextRaw(BACK), c2.GetTextRaw(BACK))

    def _cmp_learned(self, c1, c2):
        return cmp(c1.GetLearned(self.focus), c2.GetLearned(self.focus))

    def _cmp_count(self, c1, c2):
        return cmp(c1.GetCount(self.focus), c2.GetCount(self.focus))
