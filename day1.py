#!env python


def revcaptcha(rotate, seed):
    return sum(int(digit) for i, digit in enumerate(seed)
               if seed[(i+rotate) % len(seed)] == digit)

if __name__ == '__main__':
    with open('day1_input.txt') as f:
        puzzle_input = f.read()
        puzzle_input = puzzle_input.strip()

    rotate1 = 1
    rotate2 = len(puzzle_input) // 2

    print(revcaptcha(rotate1, puzzle_input))
    print(revcaptcha(rotate2, puzzle_input))
