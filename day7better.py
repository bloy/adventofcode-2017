#!env python
# -*- coding: utf-8 -*-

import aoc
import re
import collections
import pprint


Program = collections.namedtuple('Program', ('name', 'weight',
                                             'total_weight', 'children'))


def parse_data(lines):
    programs = {}
    matcher = re.compile(r"^(?P<name>\w+)\s\((?P<weight>\d+)\)(?:\s+->\s+"
                         r"(?P<children>(?:[a-z]+,\s+)*\w+))?$")
    for line in lines:
        match = matcher.match(line)
        linedata = match.groupdict()
        linedata['weight'] = int(linedata['weight'])
        if linedata['children']:
            linedata['children'] = linedata['children'].split(', ')
        else:
            linedata['children'] = []
        programs[linedata['name']] = linedata
    return programs


def find_root(data):
    names = set(data.keys())
    withparents = set()
    for name in data:
        withparents.update(set(data[name]['children']))
    return list(names - withparents)[0]


def build_tree(data, root=None):
    if not root:
        root = find_root(data)

    name = root
    weight = data[root]['weight']
    children = tuple(build_tree(data, child) for child in data[root]['children'])
    total_weight = weight + sum(child.total_weight for child in children)
    return Program(
        name=name,
        weight=weight,
        total_weight=total_weight,
        children=children,
    )


def printable_tree(tree):
    return (tree.name, tree.weight, tree.total_weight,
            tuple(printable_tree(child) for child in tree.children))


def solve1(data):
    return find_root(data)


def solve2(data):
    tree = build_tree(data)
    pprint.pprint(printable_tree(tree))


lines = (
    "pbga (66)",
    "xhth (57)",
    "ebii (61)",
    "havc (66)",
    "ktlj (57)",
    "fwft (72) -> ktlj, cntj, xhth",
    "qoyq (66)",
    "padx (45) -> pbga, havc, qoyq",
    "tknk (41) -> ugml, padx, fwft",
    "jptl (61)",
    "ugml (68) -> gyxo, ebii, jptl",
    "gyxo (61)",
    "cntj (57)",
)


if __name__ == '__main__':
    # lines = aoc.input_lines(day=7)
    data = parse_data(lines)
    print(solve1(data))
    print(solve2(data))
