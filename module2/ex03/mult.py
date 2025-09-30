#!/usr/bin/env python3
first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))

result = first * second

status = ["positive", "negative"]
print(first, "x", second, "=", result)
print(f"The result is {' and '.join(status[0:2]) if result == 0 else status[result < 0]}")
