#!env python

import aoc
import collections
import copy
import pprint


Scanner = collections.namedtuple('Scanner', 'pos vector traverse')


def parse_data(lines):
    scanners = {}
    maxlayer = 0
    for line in lines:
        layer, traverse = line.split(': ')
        layer = int(layer)
        if maxlayer < layer:
            maxlayer = layer
        scanners[layer] = Scanner(pos=0, vector=1, traverse=int(traverse))
    return maxlayer, scanners


def advance_state(layers):
    for layer in layers:
        scanner = layers[layer]
        newpos = scanner.pos + scanner.vector
        newvector = scanner.vector
        if newpos < 0 or newpos >= scanner.traverse:
            newvector = -1 * scanner.vector
            newpos = scanner.pos + newvector
        layers[layer] = Scanner(pos=newpos, vector=newvector,
                                traverse=scanner.traverse)
    return layers


def simulate(layers, maxlayer):
    layers = copy.deepcopy(layers)
    collisions = []
    for t in range(maxlayer + 1):
        if t in layers and layers[t].pos == 0:
            collisions.append((t, layers[t].traverse))
        layers = advance_state(layers)
    return sum((a * b) for a,b in collisions)


def solve1(data):
    maxlayer, layers = data
    return simulate(layers, maxlayer)


def solve2(data):
    t = 0
    maxlayer, layers = data
    caught = simulate(layers, maxlayer)
    while caught > 0:
        print(t, caught)
        t += 1
        layers = advance_state(layers)
        caught = simulate(layers, maxlayer)
    return t



lines = [
    "0: 3",
    "1: 2",
    "4: 6",
    "6: 4",
]


if __name__ == '__main__':
    # lines = aoc.input_lines(day=13)
    data = parse_data(lines)
    pprint.pprint(solve1(data))
    pprint.pprint(solve2(data))
