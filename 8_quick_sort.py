# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def quicksort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    sum1 = int(sum(array)/len(array))
    print(sum1)



def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
