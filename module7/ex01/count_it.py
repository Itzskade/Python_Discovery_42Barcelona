#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv)}")
    for arg in sys.argv[1:]:
        print(f"{arg}: {len(arg)}")
