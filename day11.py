#!/usr/bin/env python3
# AdventOfCode 2015 Day 11

import sys

def inc_str(istr):
    iarr = list(istr)
    cind = -1
    done = False
    while not done:
        rd = iarr[cind]
        if rd != 'z':
            iarr[cind] = chr(ord(rd)+1)
            done = True
        else:
            iarr[cind] = 'a'
# need to carry
            done = False
            cind -= 1
            if cind < -len(istr):
                done = True
                iarr.insert(0,'a')
                
    ostr = ''.join(iarr)
    return ostr
        
orig = sys.argv[1]

originc = inc_str(orig)
print("{}".format(originc))