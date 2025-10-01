#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print("none")
for arg in sys.argv[1:]:
    if arg.isalpha():
        print(arg)
        break
