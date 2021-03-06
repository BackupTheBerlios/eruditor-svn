========
ērudītor
========
--------------------------
A vocabulary training tool
--------------------------

:Author: Alexander Lee <alexlee (at) uchicago (dot) edu>
:Version: $Rev$
:Date: $Date$

.. contents::

Introduction
============

**ērudītor** is a card-based learning system, intended to help students of
the Classics work on their Greek and Latin vocabulary. This project was
inspired by and closely resembles Pauker_, but it is implemented in a
different language and toolkit, and it has special features for
inputting Greek and Latin cards.

.. _Pauker: http://pauker.sourceforge.net/

ērudītor is `free software`_, licensed under the GNU General Public
License. See the licensing_ section for more information.

.. _free software: http://www.fsf.org/licensing/essays/free-sw.html

Here are some screenshots_.

.. _screenshots: shots.html

How it works
============

Lessons
-------

Cards are organized into *lessons*. Each lesson contains a library of
cards. These are organized into various *piles*, or *stacks*:

1. *summary* – All of the cards
2. *unlearned* – Cards that you don't yet know
3. *ultrashort* – (Used when learning cards: ultra-shortterm memory)
4. *shortterm* – (Used when learning cards: shortterm memory)
5. *learnedN* – Stacks of learned cards. There can be several levels,
   depending on how many times you've gone over a card.

As you learn cards, they move between the various stacks. Also, after a
certain amount of time learned cards eventually *expire*; that is,
you'll have to test yourself to see if you still remember them.

Cards
-----

Each *card* has three sides:

1. *front* – the head word / dictionary entry
2. *middle* – principle parts (for verbs); genitive sg and gender (for
   nouns); etc.
3. *back* – the definition or meaning

The front and middle sides are displayed in the lesson's language, while
the back is in English.

Additionally, there's an optional *section* entry, which lets you
associate for instance a textbook unit number or classification (this is
helpful when sorting lists).

Language support
----------------

Currently, there is built-in support for three types of lessons: (1)
Greek, (2) Latin, and (3) Unicode/Plain. Some notes on each:

	**Greek** lessons use the TLG_'s `Beta Code`_ encoding scheme, with
	some modifications: (a) Lower-case characters represent lower-case
	letters, (b) You don't need the asterisk (*) before capital letters
	– just precede the capital letter with your diacritics. Some
	examples:

		| poli\_/ths = πολίτης [ῑ]
		| )Aqhnai=os = Ἀθηναῖος
		| Ai)/guptos = Αἴγυπτος
		| )Ai+dwneu/s = Ἀϊδωνεύς

	.. _TLG: http://www.tlg.uci.edu/
	.. _Beta Code: http://www.tlg.uci.edu/BetaCode.html

	**Latin** lessons use a basic method for representing long vowels:
	they are marked with a capital. (Unfortunately, this may interefere
	with real capitals that you might want in your cards. If this is a
	big deal, then use the Unicode/Plain method described below.) An
	example:

		| ErudItor = ērudītor

	**Unicode** (or *Plain*) lessons just have plain text that isn't
	interpreted or modified. Use this if you already have ways of
	entering non-Latin characters:

		| Ἀθηναῖος = Ἀθηναῖος
		| русский = русский 

There can be any number of lesson types, depending on what you are
learning. It's just a matter of people programming the support. See the
`Help Wanted`_ section below.

	*Tip* The character translations (such as with Greek and Latin) are
	applied to the front and middle of cards, but not the backs. In the
	text for the front or middle, text between {curly braces} doesn't
	get processed.

Learning process
----------------

Similar to other card-based training software, ērudītor employs the
Leitner training system. The cards are organized into stacks, based on
whether or not you know them, and how many times you've correctly
answered them.

Alternate focus
---------------

Since each card has three sides, the student has three possible targets
when learning. S/he can choose to focus on learning the backs
(word → definition), the fronts (definition → word), or the middles
(word+definition → extra info).

The ability to study the middles can be really helpful. This way the
student can learn such important bits as:

1. for *nouns*: gen sg, gender
2. for *adjectives*: gender endings for two or three termination
3. for *verbs*: principle parts

Getting started
===============

System requirements
-------------------

ērudītor should run on any operating system that supports Python and
wxPython. This encompasses a wide range of platforms, including:

- GNU/Linux (all distributions; the author likes Ubuntu_ and
  `Debian GNU/Linux`_)
- NetBSD, FreeBSD, etc.
- Windows 2000/XP
- Mac OS X (10.3 and up)

Note that due to lack of proper Unicode support, Mac OS X 10.2 and lower
are not supported.

.. _Ubuntu: http://www.ubuntu.com/
.. _Debian:
.. _Debian GNU/Linux: http://www.debian.org/

Download
--------

Releases are available at
http://developer.berlios.de/project/showfiles.php?group_id=3469.

This project is stored in a Subversion_ repository. For more info see
http://developer.berlios.de/svn/?group_id=3469.

.. _Subversion: http://subversion.tigris.org/

Installation
------------

Ubuntu and Debian
`````````````````

::

	apt-get install libwxgtk2.5.3-python python-reportlab

Unpack ``eruditor-X.X.tar.gz`` into an appropriate place (in your home
folder, or in ``/usr/local``), then run ``python Eruditor.py``.

It's just that easy.

Other UNIX (Linux, BSDs)
````````````````````````

First you'll need to get Python (http://www.python.org/). Most systems
should already have it installed, but if not, or if you have a version
before 2.4 installed, you'll need to install or upgrade.

You'll also need wxPython (http://wxpython.org/).

And if you want the PDF Study List functionality (under development),
then you should also download and install ``ReportLab_1_20.tgz`` from
http://www.reportlab.org/downloads.html.

	**NB** As always, Linux users should first try their distribution's
	package management system. BSD users should use ``ports``.

Unpack ``eruditor-X.X.tar.gz`` into an appropriate place (in your home
folder, or in ``/usr/local``), then run ``python Eruditor.py``.

Mac OS X
````````

Again, only versions 10.3 and higher are supported. Starting with
version 10.3, a suitable build of Python is included in the operating
system. So you'll just need to get the wxPython support:
http://wxpython.org/download.php#binaries

And scroll down to Mac OS X, get the ``osx-unicode`` package from the
"Panther" column.

Unpack ``eruditor-X.X.zip`` into an appropriate place (such as
``/Applications`` or in your home folder), then double-click on
``Eruditor.py``.

Windows 2000/XP
```````````````

Download and run the "Python 2.4 Windows installer"
(http://www.python.org/download/).

For wxPython, go to http://wxpython.org/download.php#binaries and get
``win32-unicode`` from the "Python 2.4" column.

And optionally, get ``ReportLab_1_20.zip`` from
http://www.reportlab.org/downloads.html.

Unpack ``eruditor-X.X.zip`` into an appropriate place (such as
``C:\Program Files\``, or your home folder, or your desktop), then
double-click on ``Eruditor.py``.

Todo List
=========

The following features are being worked on.

Export
------

1. PDF study sheet [#]_
2. Plain text study sheet
3. Text file (tab-delim, CSV, etc)

.. [#]
	Printable worksheet of 'active' words. Program will randomize active
	words list, then generate a PDF that can be folded up for easy study
	on-the-go.

Import
------

1. Pauker XML file format
2. Text file (tab-delim, CSV, etc)

Help Wanted
===========

I would appreciate help in any of the following forms:

- *Bug testing*. This is fairly new software. I wrote the bulk of it
  over spring break, 20050320–26, when I had some spare time.

- *Comments, feature requests, and suggestions*. I am less of an
  interface designer than a programmer, so I bet people can think up
  some nice interface improvements, at least.

- *Programming help*. If you'd really like to get involved, feel free to
  email me. I wouldn't mind sharing the joy. The code's out there, so
  havealook.

Also, I think it would be great if there were a standard library of
lessons that students could download and use. So far I've thought of:

GREEK
	- Vocab from Mastronarde's *Introduction to Attic Greek*. Done
	  by-the-unit. Separate list for verbs with their principle parts.

	- Campbell's *Classical Greek Prose: A Basic Vocabulary*. (Copyright
	  issues? Email me if you have any ideas...)

	- Verb list from Smyth.

	- Word list from Sidgwick or some other prose comp book.

LATIN
	- Wheelock? Cambridge Latin Course? Do these by-the-unit.

	- Word list from *Bradley's Arnold*. This could help immensely for
	  students taking prosecomp.

	- Latin word lists assembled in part by H. Pinkster (don't know the
	  title; will look into this)

GERMAN
	- April Wilson's *German Quickly*. I've already done Appendix B,
	  "Important Words". I think it will be worth it to do Appendix K,
	  "General and Humanities Vocabulary", also.

If anyone's willing to work on these, please email me. I'll post contact
info here so people can collaborate on the various lessons.  Ideas about
efficient importing methods would be nice, too. I'm planning to at least
have importing of tab-delimited and CSV files – eventually.

*Ideally, these lists would also take into account vowel length. So if
you are putting together lessons, please try to mark them!*

For Developers
==============

Language, toolkits, platform
----------------------------

ērudītor is written in Python, using the wxPython toolkit. I use vim_ to
edit the source and wxGlade_ to build the interface.

.. _vim: http://www.vim.org/
.. _wxGlade: http://wxglade.sourceforge.net/

My development system is running Ubuntu_ (variant of `Debian GNU/Linux`_).

Email me if you want more details or would like to help out.

Also, check out the `berliOS project page`_.

.. _berliOS project page: http://developer.berlios.de/projects/eruditor/

Licensing
=========

ērudītor is licensed under the GPL_:

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation.
	
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

.. _GPL: http://www.fsf.org/

----------

©2005 Alexander Lee ~ `valid XHTML`_ ~ `valid CSS`_

.. image:: http://developer.berlios.de/bslogo.php?group_id=3469
	:height: 32
	:width: 124
	:alt: BerliOS Developer Logo
	:target: http://developer.berlios.de

.. _valid XHTML: http://validator.w3.org/check?uri=referer
.. _valid CSS: http://jigsaw.w3.org/css-validator/check/referer

