#!/usr/bin/env python3

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
while second != 0:
    print(f"{first} / {second} = {first / second}")
    break
print(f"{first} * {second} = {first * second}")

