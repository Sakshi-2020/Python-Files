# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 00:53:33 2021

@author: ssing
"""
#clear
student =	{
  "Name": "Falisha",
  "Age": 21
}
student.clear()
print(student)

#copy
student =	{
  "Name": "Falisha",
  "Age": 21
}
stdnt = student.copy()
print(stdnt)

#fromkeys
Subjects = ('English', 'Mathematics', 'Science')
MM = 100
SubjectMM = dict.fromkeys(Subjects, MM)
print(SubjectMM)

#get
student =	{
  "Name": "Falisha",
  "Age": 21
}
x = student.get("Name")
print(x)

#items
student =	{
  "Name": "Falisha",
  "Age": 21
}
itm = student.items()
student["Age"] = 20
print(itm)

#pop
student =	{
  "Name": "Falisha",
  "Age": 21
}
pp = student.pop("Age")
print(pp)
print(student)

#popitem
student =	{
  "Name": "Falisha",
  "Age": 21
}
ppitm = student.popitem()
print(ppitm)
print(student)

#setdefault
student = {
  "Name": "Falisha",
  "Age": 21
}
stdflt1 = student.setdefault("Age", 20)
stdflt2 = student.setdefault("Gender", "Female")
print(stdflt1)
print(stdflt2)
print(student)

#update
student = {
  "Name": "Falisha",
  "Age": 21
}
student.update({"Gender": "Female"})

#values
student =	{
  "Name": "Falisha",
  "Age": 21
}
vl = student.values()
student["Age"] = 20
print(vl)
