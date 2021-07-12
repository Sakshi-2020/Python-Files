# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:36:26 2021

@author: ssing
"""
#append
anime1 = ["Naruto", "Sasuke"]
anime1.append("Sakura")
print(anime1)
anime2 = ["Jiraiya", "Orochimaru", "Tsunade"]
anime1.append(anime2)
print(anime1)

#clear
anime2.clear()
print(anime2)

#copy
anime3 = ["Shikamaru", "Ino", "Choji"]
anime4 = anime3.copy()
print(anime4)

#count
numbers = [1, 4, 2, 9, 7, 8, 9, 3, 1, 9]
cnt = numbers.count(9)
print(cnt)

#extend
anime5 = ["Neji", "Tenten", "RockLee"]
anime5.extend(anime4)
print(anime5)

#index
x = anime5.index("Tenten")
print(x)

#insert
anime3.insert(1, "Hinata")
print(anime3)

#pop
y = anime3.pop(1)
print(anime3)
print(y)

#remove
anime3.remove("Ino")
print(anime3)

#reverse
anime5.reverse()
print(anime5)

#sort
numbers.sort()
anime5.sort()
print(numbers)
print(anime5)
