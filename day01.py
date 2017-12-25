#!/usr/bin/python3
#AdventOfCode 2015 Day 01

import sys

floor = 0
pos = 0
first = True
with open(sys.argv[1]) as f:
    for line in f:
        for ch in line:
            if ch == '(':
                floor += 1
                pos += 1
            elif ch == ')':
                floor -= 1
                pos += 1
            else:
                print("unknown symbol")

            if (first and (floor == -1)):
                print('First entered basement: {}'.format(pos))
                first = False
f.close()
 
print('End floor: {}'.format(floor))
