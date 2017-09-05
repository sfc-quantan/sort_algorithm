# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def heap(array, until, ims, left, height):
    for i in range(1, until + 1):
        parents = int(i / 2)
        child = i
        while True:
            if array[child] > array[parents]:
                array[child], array[parents] = array[parents], array[child]
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
            parents = int(parents / 2)
            child = int(child / 2)
            if child == 0:
                break
    return array


def heapsort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    height = array

    for i in range(n - 1, 0, -1):
        array = heap(array, i, ims, left, height)
        array[i], array[0] = array[0], array[i]
        print(array)
        im = plt.bar(left, height, color="#66cdaa")
        ims.append(im)

    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    heapsort(n)


if __name__ == '__main__':
    main()
