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
Greek language support. Offers a rough equivalent to the TLG's BetaCode
standard. Also does a basic conversion to sortable text (for use with cmp()).
"""

BETACODE_ALT = {

# upper

"A" :      (u"\u0391", ""),
"B" :      (u"\u0392", ""),
"G" :      (u"\u0393", ""),
"D" :      (u"\u0394", ""),
"E" :      (u"\u0395", ""),
"Z" :      (u"\u0396", ""),
"H" :      (u"\u0397", ""),
"Q" :      (u"\u0398", ""),
"I" :      (u"\u0399", ""),
"K" :      (u"\u039a", ""),
"L" :      (u"\u039b", ""),
"M" :      (u"\u039c", ""),
"N" :      (u"\u039d", ""),
"C" :      (u"\u039e", ""),
"O" :      (u"\u039f", ""),
"P" :      (u"\u03a0", ""),
"R" :      (u"\u03a1", ""),
"S" :      (u"\u03a3", ""),
"T" :      (u"\u03a4", ""),
"U" :      (u"\u03a5", ""),
"F" :      (u"\u03a6", ""),
"X" :      (u"\u03a7", ""),
"Y" :      (u"\u03a8", ""),
"W" :      (u"\u03a9", ""),

# upper w/ diacritics

")A" :     (u"\u1f08", ""),
"(A" :     (u"\u1f09", ""),
")\\A" :   (u"\u1f0a", ""),
"(\\A" :   (u"\u1f0b", ""),
")/A" :    (u"\u1f0c", ""),
"(/A" :    (u"\u1f0d", ""),
"(=A" :    (u"\u1f0f", ""),
")=A" :    (u"\u1f0e", ""),

")E" :     (u"\u1f18", ""),
"(E" :     (u"\u1f19", ""),
")\\E" :   (u"\u1f1a", ""),
"(\\E" :   (u"\u1f1b", ""),
")/E" :    (u"\u1f1c", ""),
"(/E" :    (u"\u1f1d", ""),

")H" :     (u"\u1f28", ""),
"(H" :     (u"\u1f29", ""),
")\\H" :   (u"\u1f2a", ""),
"(\\H" :   (u"\u1f2b", ""),
")/H" :    (u"\u1f2c", ""),
"(/H" :    (u"\u1f2d", ""),
")=H" :    (u"\u1f2e", ""),
"(/H" :    (u"\u1f2f", ""),

")I" :     (u"\u1f38", ""),
"(I" :     (u"\u1f39", ""),
")\\I" :   (u"\u1f3a", ""),
"(\\I" :   (u"\u1f3b", ""),
")/I" :    (u"\u1f3c", ""),
"(/I" :    (u"\u1f3d", ""),
")=I" :    (u"\u1f3e", ""),
"(=I" :    (u"\u1f3f", ""),

")O" :     (u"\u1f48", ""),
"(O" :     (u"\u1f49", ""),
")\\O" :   (u"\u1f4a", ""),
"(\\O" :   (u"\u1f4b", ""),
")/O" :    (u"\u1f4c", ""),
"(/O" :    (u"\u1f4d", ""),

"(U" :     (u"\u1f59", ""),
"(\\U" :   (u"\u1f5b", ""),
"(/U" :    (u"\u1f5d", ""),
"(=U" :    (u"\u1f5f", ""),

")W" :     (u"\u1f68", ""),
"(W" :     (u"\u1f69", ""),
")\\W" :   (u"\u1f6a", ""),
"(\\W" :   (u"\u1f6b", ""),
")/W" :    (u"\u1f6c", ""),
"(/W" :    (u"\u1f6d", ""),
")=W" :    (u"\u1f6e", ""),
"(=W" :    (u"\u1f6f", ""),

"(R" :     (u"\u1fec", ""),

# lower

"a" :      (u"\u03b1", ""),
"b" :      (u"\u03b2", ""),
"g" :      (u"\u03b3", ""),
"d" :      (u"\u03b4", ""),
"e" :      (u"\u03b5", ""),
"z" :      (u"\u03b6", ""),
"h" :      (u"\u03b7", ""),
"q" :      (u"\u03b8", ""),
"i" :      (u"\u03b9", ""),
"k" :      (u"\u03ba", ""),
"l" :      (u"\u03bb", ""),
"m" :      (u"\u03bc", ""),
"n" :      (u"\u03bd", ""),
"c" :      (u"\u03be", ""),
"o" :      (u"\u03bf", ""),
"p" :      (u"\u03c0", ""),
"r" :      (u"\u03c1", ""),
"s" :      (u"\u03c3", ""),
"j" :      (u"\u03c2", ""),
"t" :      (u"\u03c4", ""),
"u" :      (u"\u03c5", ""),
"f" :      (u"\u03c6", ""),
"x" :      (u"\u03c7", ""),
"y" :      (u"\u03c8", ""),
"w" :      (u"\u03c9", ""),

# final sigma substitution and punctuation

"s\n" :    (u"\u03c2\n", ""),
"s$" :     (u"\u03c2", ""),
"s," :     (u"\u03c2,", ""),
"s." :     (u"\u03c2.", ""),
"s:" :     (u"\u03c2\u0387", ""),
"s;" :     (u"\u03c2\u0387", ""),
"s?" :     (u"\u03c2\u037e", ""),
"s]" :     (u"\u03c2]", ""),
"s)" :     (u"\u03c2)", ""),
"s " :     (u"\u03c2 ", ""),

";" :      (u"\u0387", ""),
":" :      (u"\u0387", ""),
"?" :      (u"\u037e", ""),
"$" :      ("", ""),

# lower with diacritics

"i+" :     (u"\u03ca", ""),
"i_+" :    (u"\u03ca", u"\u1fd1"),
"u+" :     (u"\u03cb", ""),
"u_+" :    (u"\u03cb", u"\u1fe1"),

"a)" :     (u"\u1f00", ""),
"a(" :     (u"\u1f01", ""),
"a)\\" :   (u"\u1f02", ""),
"a(\\" :   (u"\u1f03", ""),
"a)/" :    (u"\u1f04", ""),
"a(/" :    (u"\u1f05", ""),
"a)=" :    (u"\u1f06", ""),
"a(=" :    (u"\u1f07", ""),
"a_)" :     (u"\u1f00", u"\u1fb1"),
"a_(" :     (u"\u1f01", u"\u1fb1"),
"a_)\\" :   (u"\u1f02", u"\u1fb1"),
"a_(\\" :   (u"\u1f03", u"\u1fb1"),
"a_)/" :    (u"\u1f04", u"\u1fb1"),
"a_(/" :    (u"\u1f05", u"\u1fb1"),

"e)" :     (u"\u1f10", ""),
"e(" :     (u"\u1f11", ""),
"e)\\" :   (u"\u1f12", ""),
"e(\\" :   (u"\u1f13", ""),
"e)/" :    (u"\u1f14", ""),
"e(/" :    (u"\u1f15", ""),

"h)" :     (u"\u1f20", ""),
"h(" :     (u"\u1f21", ""),
"h)\\" :   (u"\u1f22", ""),
"h(\\" :   (u"\u1f23", ""),
"h)/" :    (u"\u1f24", ""),
"h(/" :    (u"\u1f25", ""),
"h)=" :    (u"\u1f26", ""),
"h(=" :    (u"\u1f27", ""),

"i)" :     (u"\u1f30", ""),
"i(" :     (u"\u1f31", ""),
"i)\\" :   (u"\u1f32", ""),
"i(\\" :   (u"\u1f33", ""),
"i)/" :    (u"\u1f34", ""),
"i(/" :    (u"\u1f35", ""),
"i)=" :    (u"\u1f36", ""),
"i(=" :    (u"\u1f37", ""),
"i_)" :    (u"\u1f30", u"\u1fd1"),
"i_(" :    (u"\u1f31", u"\u1fd1"),
"i_)\\" :  (u"\u1f32", u"\u1fd1"),
"i_(\\" :  (u"\u1f33", u"\u1fd1"),
"i_)/" :   (u"\u1f34", u"\u1fd1"),
"i_(/" :   (u"\u1f35", u"\u1fd1"),

"o)" :     (u"\u1f40", ""),
"o(" :     (u"\u1f41", ""),
"o)\\" :   (u"\u1f42", ""),
"o(\\" :   (u"\u1f43", ""),
"o)/" :    (u"\u1f44", ""),
"o(/" :    (u"\u1f45", ""),

"u)" :     (u"\u1f50", ""),
"u(" :     (u"\u1f51", ""),
"u)\\" :   (u"\u1f52", ""),
"u(\\" :   (u"\u1f53", ""),
"u)/" :    (u"\u1f54", ""),
"u(/" :    (u"\u1f55", ""),
"u)=" :    (u"\u1f56", ""),
"u(=" :    (u"\u1f57", ""),
"u_)" :    (u"\u1f50", u"\u1fe1"),
"u_(" :    (u"\u1f51", u"\u1fe1"),
"u_)\\" :  (u"\u1f52", u"\u1fe1"),
"u_(\\" :  (u"\u1f53", u"\u1fe1"),
"u_)/" :   (u"\u1f54", u"\u1fe1"),
"u_(/" :   (u"\u1f55", u"\u1fe1"),

"w)" :     (u"\u1f60", ""),
"w(" :     (u"\u1f61", ""),
"w)\\" :   (u"\u1f62", ""),
"w(\\" :   (u"\u1f63", ""),
"w)/" :    (u"\u1f64", ""),
"w(/" :    (u"\u1f65", ""),
"w)=" :    (u"\u1f66", ""),
"w(=" :    (u"\u1f67", ""),

"a\\" :    (u"\u1f70", ""),
"a/" :     (u"\u1f71", ""),
"a_\\" :   (u"\u1f70", u"\u1fb1"),
"a_/" :    (u"\u1f71", u"\u1fb1"),
"e\\" :    (u"\u1f72", ""),
"e/" :     (u"\u1f73", ""),
"h\\" :    (u"\u1f74", ""),
"h/" :     (u"\u1f75", ""),
"i\\" :    (u"\u1f76", ""),
"i/" :     (u"\u1f77", ""),
"i_\\" :   (u"\u1f76", u"\u1fd1"),
"i_/" :    (u"\u1f77", u"\u1fd1"),
"o\\" :    (u"\u1f78", ""),
"o/" :     (u"\u1f79", ""),
"u\\" :    (u"\u1f7a", ""),
"u/" :     (u"\u1f7b", ""),
"u_\\" :   (u"\u1f7a", u"\u1fe1"),
"u_/" :    (u"\u1f7b", u"\u1fe1"),
"w\\" :    (u"\u1f7c", ""),
"w/" :     (u"\u1f7d", ""),

"a)|" :    (u"\u1f80", ""),
"a(|" :    (u"\u1f81", ""),
"a)\\|" :  (u"\u1f82", ""),
"a(\\|" :  (u"\u1f83", ""),
"a)/|" :   (u"\u1f84", ""),
"a(/|" :   (u"\u1f85", ""),
"h)|" :    (u"\u1f90", ""),
"h(|" :    (u"\u1f91", ""),
"h)/|" :   (u"\u1f94", ""),
"h(/|" :   (u"\u1f95", ""),
"h)=|" :   (u"\u1f96", ""),
"h(=|" :   (u"\u1f97", ""),
"w)|" :    (u"\u1fa0", ""),
"w(=|" :   (u"\u1fa7", ""),

"a_" :     (u"\u1fb1", ""),
"a\\|" :   (u"\u1fb2", ""),
"a|" :     (u"\u1fb3", ""),
"a/|" :    (u"\u1fb4", ""),
"a=" :     (u"\u1fb6", ""),
"a=|" :    (u"\u1fb7", ""),

"h\\|" :   (u"\u1fc2", ""),
"h|" :     (u"\u1fc3", ""),
"h/|" :    (u"\u1fc4", ""),
"h=" :     (u"\u1fc6", ""),
"h=|" :    (u"\u1fc7", ""),

"i_" :     (u"\u1fd1", ""),
"i+\\" :   (u"\u1fd2", ""),
"i+/" :    (u"\u1fd3", ""),
"i=" :     (u"\u1fd6", ""),
"i+=" :    (u"\u1fd7", ""),
"i_+\\" :  (u"\u1fd2", u"\u1fd1"),
"i_+/" :   (u"\u1fd3", u"\u1fd1"),

"u_" :     (u"\u1fe1", ""),
"u+\\" :   (u"\u1fe2", ""),
"u+/" :    (u"\u1fe3", ""),
"r)" :     (u"\u1fe4", ""),
"r(" :     (u"\u1fe5", ""),
"u=" :     (u"\u1fe6", ""),
"u+=" :    (u"\u1fe7", ""),
"u_+\\" :  (u"\u1fe2", u"\u1fe1"),
"u_+/" :   (u"\u1fe3", u"\u1fe1"),

"w\\|" :   (u"\u1ff2", ""),
"w|" :     (u"\u1ff3", ""),
"w/|" :    (u"\u1ff4", ""),
"w=" :     (u"\u1ff6", ""),
"w=|" :    (u"\u1ff7", ""),

}


# Pattern for string comparisons
# Assumes string has been put into lowercase first
BETACODE_CMP = {

"a" : "a",
"b" : "b",
"g" : "c",
"d" : "d",
"e" : "e",
"z" : "f",
"h" : "g",
"q" : "h",
"i" : "i",
"k" : "j",
"l" : "k",
"m" : "l",
"n" : "m",
"c" : "n",
"o" : "o",
"p" : "p",
"r" : "q",
"s" : "r",
"j" : "s",
"t" : "t",
"u" : "u",
"f" : "v",
"x" : "w",
"y" : "x",
"w" : "y",
")" : "",
"(" : "",
"/" : "",
"\\" : "",
"=" : "",
"|" : "",
"_" : "",
"+" : "",

}
