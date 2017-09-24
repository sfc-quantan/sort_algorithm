# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def bubblesort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    height = array
    ims = []
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            im = plt.bar(left, height, color="#66cadd")
            ims.append(im)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    ani.save("bubble.gif", writer="imagemagick")
    plt.close()


def main():
    n = parse()
    bubblesort(n)


if __name__ == '__main__':
    main()
