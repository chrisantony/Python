# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 14:36:23 2015

@author: cantony
"""
actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

for actor, character in actors.iteritems():
    print 'name of the actor is {0} and the character played is {1}'.format(actor, character)
    
    
for n in range(1, 100):
    if n % 3 == 0:
        print (n)

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
