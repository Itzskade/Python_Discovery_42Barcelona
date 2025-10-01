#!/usr/bin/env python3

entry = input("Give me a number: ")
try:
    number = float(entry)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That's not a valiod number.")
