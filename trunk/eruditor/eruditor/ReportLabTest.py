# -*- coding: utf-8 -*-

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('NAU', 'newathu.ttf'))
from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.setFont('NAU', 32)
c.drawString(10, 150, "Some text encoded in UTF-8")
c.drawString(10, 100, "ērudītor – ἄνθρωπος")
c.showPage()
c.save()
