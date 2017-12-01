#!env python

with open('day1_input.txt') as f:
    puzzle_input = f.read()
    puzzle_input = puzzle_input.strip()

summable1 = []
summable2 = []
index1 = 1
index2 = len(puzzle_input) // 2

for i, digit in enumerate(puzzle_input):
    if puzzle_input[(i+index1) % len(puzzle_input)] == digit:
        summable1.append(int(digit))
    if puzzle_input[(i+index2) % len(puzzle_input)] == digit:
        summable2.append(int(digit))

print(summable1)
print(sum(summable1))

print(summable2)
print(sum(summable2))
