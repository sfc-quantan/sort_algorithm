from random import shuffle
from parser_n import parse


def make_array():
    n = parse()
    a = list(range(1, n + 1))
    shuffle(a)
    return a
