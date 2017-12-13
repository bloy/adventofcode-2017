#!env python

import aoc
import collections
import copy
import pprint


def parse_data(lines):
    scanners = {}
    maxlayer = 0
    for line in lines:
        layer, traverse = line.split(': ')
        layer = int(layer)
        traverse = int(traverse)
        if maxlayer < layer:
            maxlayer = layer
        scannerpositions = (tuple(range(traverse))
                            + tuple(range(traverse-2, 0, -1)))
        scanners[layer] = (traverse, scannerpositions)
    return maxlayer, scanners


def position_at(positions, time):
    return positions[time % len(positions)]


def simulate(layers, maxlayer, start=0):
    collisions = []
    for t in range(maxlayer + 1):
        if t in layers and position_at(layers[t][1], t+start) == 0:
            collisions.append((t, layers[t][0]))
    return sum((a * b) for a,b in collisions)


def solve1(data):
    maxlayer, layers = data
    return simulate(layers, maxlayer)


def solve2(data):
    t = 0
    maxlayer, layers = data
    caught = simulate(layers, maxlayer, start=t)
    while caught > 0:
        print(t, caught)
        t += 1
        caught = simulate(layers, maxlayer, start=t)
    return t



lines = [
    "0: 3",
    "1: 2",
    "4: 6",
    "6: 4",
]


if __name__ == '__main__':
    #lines = aoc.input_lines(day=13)
    data = parse_data(lines)
    pprint.pprint(solve1(data))
    # pprint.pprint(solve2(data))
