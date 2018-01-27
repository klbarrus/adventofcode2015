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

def search_straight(istr):
    ret = False
    for x in range(len(istr)-2):
        c1 = ord(istr[x])
        c2 = ord(istr[x+1])
        c3 = ord(istr[x+2])
        if c2 == c1+1 and c3 == c2+1:
            ret = True
            break
    return ret

def search_iol(istr):
    ret = False
    for x in istr:
        if x == 'i' or x == 'o' or x == 'l':
            ret = True
            break
    return ret

orig = sys.argv[1]

originc = inc_str(orig)
print("{}".format(originc))
print("iol found: {}".format(search_iol(originc)))
print("straight: {}".format(search_straight(originc)))