#!/usr/bin/env python3


def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, Guido!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1+num2
result=add(45,50)
print(result)

def halve(number):
    return number / 2
