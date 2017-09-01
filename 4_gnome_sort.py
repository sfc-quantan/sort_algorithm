# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  parser_n import parse

def gnomesort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []

    for i in range(1, n):
        print(array)
        for j in range(i,0,-1):
            if array[j - 1] >  array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]





def main():
    n = parse()
    gnomesort(n)

if __name__ == '__main__':
    main()
