#!/usr/bin/env python3

import sys

char = 'z'
if len(sys.argv) != 2:
    print("none")
else:
    for z in sys.argv[1]:
        if (z == char):
            print(char, end="")
    print(end='\n')

