# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 20:43:01 2021

@author: ssing
"""
#One way to do this is to represent each employee as a list.
#Each employee's name, age, position, and the year they started working.
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

#Keyword pass: placeholder indicating where code will eventually go.
#It allows you to run this code without Python throwing an error.
class Dog:
    pass

#The properties of class objects are defined in a method called .__init__().
#self.name = name creates an attribute called name and assigns to it the value of the name parameter.
#self.age = age creates an attribute called age and assigns to it the value of the age parameter.
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

#Class and Instance Attributes
#Class attributes: Attributes that have the same value for all class instances.
#A class attribute is defined by assigning a value to a variable name outside of .__init__().
class Dog:
    # Class attribute
    species = "Canis lupus familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

#.description() returns a string displaying the name and age of the dog.
      # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

#.speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.        
    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
miles = Dog("Miles", 4, "Jack Russell Terrier")
#.description() returns a string containing information about the Dog instance miles.
print(miles.description())

#.speak() returns a string containing the dog’s name miles and the sound the miles makes.
print(miles.speak("Woof Woof"))
print(miles.speak("Bow Wow"))

#To determine the class of an instance, the built-in isinstance() can be used.
print(isinstance(miles, Dog))

buddy = Dog("Buddy", 9, "Dachshund")
print(buddy.speak("Yap"))

jack = Dog("Jack", 3, "Bulldog")
print(jack.speak("Woof"))

jim = Dog("Jim", 5, "Bulldog")
print(jim.speak("Woof"))

#Parent Classes vs Child Classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
#To create a child class, create new class with its own name and then put the name of the parent class in parentheses.
class Dachshund(Dog):
    pass



#Extend the Functionality of a Parent Class
#To override a method defined on the parent class, define a method with the same name on the child class.
#.speak() is defined on the JackRussellTerrier class with the default argument for sound set to "Arf".
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

#If the method is not present in child class, then only it will propagate to the parent class.
#To access the parent class from inside a method of a child class by using super():
class Bulldog(Dog):
    def speak(self, sound="Woof Woof"):
        return super().speak(sound)

jack = Bulldog("Jack", 3)
print(jack.speak())
    
#Instances of child classes inherit all of the attributes and methods of the parent class:
print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

#To determine which class a given object belongs to, you can use the built-in type():
print(type(miles))

#.speak() can be on a JackRussellTerrier instance without passing an argument to sound:
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())


    
