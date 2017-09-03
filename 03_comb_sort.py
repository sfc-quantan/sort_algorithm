# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def combsort(n):
    h = int(n / 2)
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    for i in range(h, -1, -1):
        for j in range(n - i):
            height = array
            print(array)
            im = plt.bar(left, height, color="#66cdaa")
            ims.append(im)
            if array[j] < array[j + i]:
                array[j], array[j + i] = array[j + i], array[j]
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    combsort(n)

if __name__ == '__main__':
    main()

