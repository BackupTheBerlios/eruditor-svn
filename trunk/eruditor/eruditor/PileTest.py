#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# A test application for doing painting.
# This is for the piles widget in the flashcard app.

import wx
import PilesPanel
import Lesson

class PilesFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Piles", size=(200,200),
                style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.panel = PilesPanel.PilesPanel(self, -1)

if __name__ == '__main__':
    lesson = Lesson.Lesson(filename="test.xml")
    app = wx.PySimpleApp()
    frame = PilesFrame(None)
    frame.Show(True)
    frame.panel.Update(lesson)
    app.MainLoop()
