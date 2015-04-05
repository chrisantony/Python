# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 17:28:47 2015

@author: cantony
"""

for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print "fizzbuzz"
    elif n % 3 == 0:
        print "fizz"
    elif n % 5 == 0:
        print "buzz"
    else:
        print (n)
        