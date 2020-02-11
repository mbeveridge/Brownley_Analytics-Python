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