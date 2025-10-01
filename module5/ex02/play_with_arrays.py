#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]

suma = 2
print(array)
new_array = [number + suma for number in array if number > 5]

print(new_array)
