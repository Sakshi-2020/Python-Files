# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:41:17 2021

@author: ssing
"""

#add
objects1 = {"table", "chair", "pen", "banana"}
objects1.add("pencil")
#If the element already exists, the add() method does not add the element.
objects1.add("pen")
print(objects1)

#clear
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy
objects2 = objects1.copy()
print(objects2)

#difference
objects3 = {"table", "banana", "keyboard"}
diff1 = objects3.difference(objects1) 
diff2 = objects1.difference(objects3) 
print(diff1)
print(diff2)

#difference_update
objects3.difference_update(objects1)
print(objects3)

#discard
objects2.discard("table")
print(objects2)

#intersection
insc1 = objects2.intersection(objects1)
print(insc1)
#for three sets
objects4 = {"bed", "mouse", "keyboard", "banana"}
insc2 = objects2.intersection(objects3, objects4)
print(insc2)

#intersection_update
fruits = {"apple", "banana", "cherry"}
brands = {"google", "microsoft", "apple"}
fruits.intersection_update(brands) 
print(fruits)

#isdisjoint
fruits = {"apple", "banana", "cherry"}
browsers = {"chrome", "edge", "safari"}
isdjnt = fruits.isdisjoint(browsers) 
print(isdjnt)

#issubset
fruits = {"apple", "banana", "cherry"}
brands = {"google", "microsoft", "apple"}
issbst = fruits.issubset(brands) 
print(issbst)

#issuperset
fruits = {"apple", "banana", "cherry"}
brands = {"google", "microsoft", "apple"}
issprst = fruits.issuperset(brands) 
print(issprst)

#pop
pp = fruits.pop() 
print(fruits)
print(pp)

#remove
fruits = {"apple", "banana", "cherry", "orange"}
fruits.remove("orange")
print(fruits)

#symmetric_difference
fruits = {"apple", "banana", "cherry"}
brands = {"google", "microsoft", "apple"}
symmdiff = fruits.symmetric_difference(brands) 
print(symmdiff)

#symmetric_difference_update
fruits = {"apple", "banana", "cherry"}
brands = {"google", "microsoft", "apple"}
fruits.symmetric_difference_update(brands) 
print(fruits)

#union
fruits = {"apple", "banana", "cherry"}
un = fruits.union(brands) 
print(un)

#update
fruits = {"apple", "banana", "cherry"}
brands = {"google", "microsoft", "apple"}
fruits.update(brands) 
print(fruits)

