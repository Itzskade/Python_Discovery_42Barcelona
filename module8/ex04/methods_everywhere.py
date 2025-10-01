#!/usr/bin/env python3

import sys

def shrink(arg):
    print(arg[:8])

def enlarge(arg):
    print(arg + "z" * (8 - len(arg)))

args = sys.argv[1:]
if len(sys.argv) < 2:
    print('none')
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
