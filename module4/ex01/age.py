#!/usr/bin/env python3

years = {10, 20, 30}
age = int(input("Please tell me your age: "))
print(f"You are currently: {age} years old.")

for y in years:
          future_year = age + y
          print(f"In {y} years, you'll be {future_year} years old.")

