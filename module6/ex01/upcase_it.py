#!/usr/bin/env python3

import sys

txt = sys.argv
if (len(sys.argv) <= 1): 
    print("none")
for arg in sys.argv[1:]:
    upper = arg.upper()
    print(f"{upper}")
