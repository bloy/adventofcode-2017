#!env python

import aoc
import collections
import pprint


Point = collections.namedtuple('Point', ['x', 'y', 'z'])


def part2point(part):
    x, y, z = part[3:-1].split(',')
    return Point(x=int(x), y=int(y), z=int(z))


def parse_data(lines):
    particles = []
    for num, line in enumerate(lines):
        p, v, a = line.split(', ')
        particles.append({
            "num": num,
            "p": part2point(p),
            "v": part2point(v),
            "a": part2point(a),
        })
    return particles


def num_at_tick(tick, p, v, a):
    delta = sum(v + t * a for t in range(1, tick+1))
    return p + delta


def pos_at_tick(tick, particle):
    return Point(
        x=num_at_tick(tick, particle['p'].x, particle['v'].x, particle['a'].x),
        y=num_at_tick(tick, particle['p'].y, particle['v'].y, particle['a'].y),
        z=num_at_tick(tick, particle['p'].z, particle['v'].z, particle['a'].z),
    )


def distance_at_tick(tick, particle):
    pos = pos_at_tick(tick, particle)
    return abs(pos.x) + abs(pos.y) + abs(pos.z)


def solve1(data):
    return data


def solve2(data):
    pass


lines = [
    'p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>'
]


if __name__ == '__main__':
    # lines = aoc.input_lines(day=20)
    data = parse_data(lines)
    pprint.pprint(data[0])
    for tick in range(10):
        pprint.pprint(pos_at_tick(tick, data[0]))
    # pprint.pprint(solve1(data))
    # pprint.pprint(solve2(data))
