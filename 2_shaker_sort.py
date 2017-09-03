# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def shakersort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    for i in range(n - 1):
        array2 = array[:]
        if i % 2 == 0:
            for j in range(n - 1):
                height = array
                print(array)
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        else:
            for j in range(n - 1, 0, -1):
                height = array
                print(array)
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
                if array[j] > array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
            if array2 == array:
                break
    ani = animation.ArtistAnimation(fig, ims, interval=100)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    shakersort(n)

if __name__ == '__main__':
    main()
