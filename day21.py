#!env python

import aoc
import collections
import itertools
import pprint


def flip(chunk, vertical=True):
    size = int(len(chunk) ** 0.5)
    if vertical:
        return "".join(reversed(list(chunk[x*size:x*size+size]
                                for x in range(size))))
    return "".join("".join(reversed(chunk[x*size:x*size+size]))
                   for x in range(size))

def rotate(chunk):
    size = int(len(chunk) ** 0.5)
    return "".join("".join(reversed(chunk[x:9:size])) for x in range(size))


def rotates_and_flips(chunk):
    trans = set()
    trans.add(rotate(chunk))
    trans.add(rotate(rotate(chunk)))
    trans.add(rotate(rotate(rotate(chunk))))
    trans.add(flip(chunk))
    trans.add(rotate(flip(chunk)))
    trans.add(rotate(rotate(flip(chunk))))
    trans.add(rotate(rotate(rotate(flip(chunk)))))
    trans.add(flip(chunk, False))
    trans.add(rotate(flip(chunk, False)))
    trans.add(rotate(rotate(flip(chunk, False))))
    trans.add(rotate(rotate(rotate(flip(chunk, False)))))
    return tuple(trans)


def parse_data(lines):
    transforms = {}
    for line in lines:
        ingrid, outgrid = ["".join(part.split('/'))
                           for part in line.split(' => ')]
        transforms[ingrid] = outgrid
    for key, value in tuple(transforms.items()):
        for change in rotates_and_flips(key):
            if change not in transforms:
                transforms[change] = value
    return transforms


def solve1(start, data):
    return data


def solve2(start, data):
    pass


def print_chunk(chunk):
    size = int(len(chunk) ** 0.5)
    print("\n".join(chunk[x*size:x*size+size] for x in range(size)))


lines = [
    '../.# => ##./#../...',
    '.#./..#/### => #..#/..../..../#..#',
]

start = (
    '.#.'
    '..#'
    '###'
)

if __name__ == '__main__':
    lines = aoc.input_lines(day=21)
    data = parse_data(lines)
    pprint.pprint(solve1(start, data))
    pprint.pprint(solve2(start, data))
