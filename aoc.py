import os.path


def input_lines(day):
    filename = os.path.join(os.path.dirname(__file__), 'input',
                            'day{0}.txt'.format(day))
    with open(filename) as open_file:
        for line in open_file:
            yield line.strip()
