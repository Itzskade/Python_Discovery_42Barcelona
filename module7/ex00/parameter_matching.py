#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = str(input("What was the parameter? "))
    if (param == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")
