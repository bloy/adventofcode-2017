#!env python

import aoc
import collections
import pprint
import re


ISINT = re.compile(r'^-?[0-9]+$')


def parse_data(lines):
    return [line.split() for line in lines]


def valueof(v, registers):
    if v is None:
        return None
    if ISINT.match(v):
        return int(v)
    return registers[v]


def solve1(data):
    registers = collections.defaultdict(int)
    pc = 0
    soundplayed = 0
    while 0 <= pc < len(data):
        instr = data[pc][0]
        v1 = data[pc][1]
        v2 = data[pc][2] if len(data[pc]) > 2 else None
        pc += 1

        if instr == 'snd':
            soundplayed = valueof(v1, registers)
        elif instr == 'rcv':
            if valueof(v1, registers) != 0:
                return ('Last sound played', soundplayed)
        elif instr == 'set':
            registers[v1] = valueof(v2, registers)
        elif instr == 'add':
            registers[v1] += valueof(v2, registers)
        elif instr == 'mul':
            registers[v1] *= valueof(v2, registers)
        elif instr == 'mod':
            registers[v1] = registers[v1] % valueof(v2, registers)
        elif instr == 'jgz':
            if valueof(v1, registers) > 0:
                pc += valueof(v2, registers) - 1

    return "terminated"


def solve2(data):
    pass


lines = [
    'set a 1',
    'add a 2',
    'mul a a',
    'mod a 5',
    'snd a',
    'set a 0',
    'rcv a',
    'jgz a -1',
    'set a 1',
    'jgz a -2',
]


if __name__ == '__main__':
    lines = aoc.input_lines(day=18)
    data = parse_data(lines)
    pprint.pprint(solve1(data))
    pprint.pprint(solve2(data))
