#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
suma = 2

print(array)
new_array = set(number + suma for number in array if number > 5)
orden_deseado = [10, 11, 50, 24]
print("{" + ", ".join(str(x) for x in orden_deseado if x in new_array) + "}")
