# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:32:48 2021

@author: ssing
"""
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    option = input("Enter operator: ")

    if option == '1':
        n = int(input("How many numbers do you want to add: "))
        sum = 0
        for x in range(n):
            num = int(input("Enter number: "))
            sum = sum + num
        print(sum)
        break;
    elif option == '2':
        num_one = int(input("Enter 1st number: "))
        num_two = int(input("Enter 2nd number: "))
        print(num_one - num_two)
        break;
    elif option == '3':
        n = int(input("How many numbers do you want to multiply: "))
        mul = 1
        for x in range(n):
            num = int(input("Enter number: "))
            mul = mul * num
        print(mul)
        break;
    elif option == '4':
        num_one = int(input("Enter 1st number: "))
        num_two = int(input("Enter 2nd number: "))
        print(num_one / num_two)
        break;
    else:
        print("Invalid Operator")
        