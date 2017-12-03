#!env python

import itertools
import math
import pprint

def rings():
    prevringmax = 0
    for ring in itertools.count(0):
        ringmax = ((ring*2)+1)**2
        ringmin = prevringmax + 1
        prevringmax = ringmax
        yield(ring, range(ringmin, ringmax+1))


def find_ring(num):
    for ring in rings():
        if num in ring[1]:
            return ring


def solve1(num):
    ring, ringrange = find_ring(num)
    if ring == 0:
        return 0;
    rangedistance = zip(ringrange, itertools.cycle(
        itertools.chain(range(ring*2-1, ring-1, -1), range(ring+1, ring*2+1))))
    for testnum, dist in rangedistance:
        if testnum == num:
            return dist


if __name__ == '__main__':
    space = 361527
    examples = (1, 2, 3, 12, 23, 1024, space)
    for ex in examples:
        print(ex, solve1(ex))
