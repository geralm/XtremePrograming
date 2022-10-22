
# a simple parser for python. use get_number() and get_word() to read
import scipy
import numpy


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# numpy and scipy are available for use

# Read the number of testcases
T = get_word()

# Process each test case
for t in range(T):
    N = get_word()

    answer = 0
    # Read each offset
    # TODO: You will need to figure out how to
    # process the offset and change the variable answer
    for n in range(N):
        D = get_word()

    # Output your answer
        print(answer)
