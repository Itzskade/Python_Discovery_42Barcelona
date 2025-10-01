#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        print(list(range(start, end + 1)))
    except ValueError:
        print("none")
