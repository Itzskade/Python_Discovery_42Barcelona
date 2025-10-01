#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print("none")
else:
    for x in sys.argv[1:]:
        if "ism" not in x:
            print(x + "ism")
        else:
            print(x)
