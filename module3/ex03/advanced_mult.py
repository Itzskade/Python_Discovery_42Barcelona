#!/usr/bin/env python3
table = 0
while(table <= 10):
    print(f"Table of {table}:", end=" ")
    count = 0
    while(count <= 10):
        result = count * table
        print(result, end=" ")
        count  += 1
    print(end='\n')
    table += 1

