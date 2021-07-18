# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:44:47 2021

@author: ssing
"""

from datetime import date

birthdate = int(input("Enter your Birth date: "))      
birthmonth = int(input("Enter your Birth month (in number): "))
birthyear = int(input("Enter your Birth year: "))

birthDate = date(birthyear, birthmonth, birthdate)

today = date.today()
age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
print("Your age:", age, "years")