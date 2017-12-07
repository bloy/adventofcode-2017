#!env python

import aoc
import collections
import pprint


def read_rows(rows):
    data = []
    for row in rows:
        row = row.split(' -> ')
        children = tuple(row[1].split(', ')) if len(row) == 2 else tuple()
        name, weight = row[0].split(' ')
        weight = int(weight[1:-1])
        data.append((name, weight, children))
    return data


def solve1(data):
    names = set()
    withparents = set()
    for row in data:
        names.add(row[0])
        withparents.update(set(row[2]))
    return names - withparents


def solve2(data):
    return None


rows = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split("\n")

if __name__ == '__main__':

    rows = [row for row in aoc.input_lines(day=7)]
    data = read_rows(rows)
    print(solve1(data))
    print(solve2(data))
