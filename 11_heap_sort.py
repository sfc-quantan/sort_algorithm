# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def heap(array):
    pass

def heapsort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []

    for i in range(n, 0, -1):
        array = heap(array)
        array[i],array[0], = array[0], array[i]

    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    heapsort(n)


if __name__ == '__main__':
    main()
