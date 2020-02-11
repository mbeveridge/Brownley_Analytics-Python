#!/usr/bin/env python3
from math import exp, log, sqrt  # Page13
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:45:49 2020

@author: markbeveridge
"""


print("Output #1: I'm excited to learn Python.")  # Page1


# Add two numbers together ...Page8
x=4
y=5
z=x+y
print("Output #2: Four plus five equals {0:d}.".format(z))


# Add two lists together ...Page8
a=[1,2,3,4]
b = ["first", "second", "third", "fourth"]
c=a+b
print("Output #3: {0}, {1}, {2}".format(a, b, c))


# Integers ...Page12
x=9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))


# Floating-point numbers ...Page12
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))


# `math` module functions ...Page13
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))


# Strings ...Page14
print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))
print("Output #15: {0:s}".format("This is a long string. Without the backslash\
 it would run off of the page on the right in the text editor and be very\
 difficult to read and edit. By using the backslash you can split the long\
 string into smaller strings on separate lines so that the whole string is easy\
 to view in the text editor."))
print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))
print("Output #17: {0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))


# operators on strings ...Page15
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))
