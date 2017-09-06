# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def shellsort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    h = [6, 4, 2, 1]
    height = array

    for i in range(len(h)):
        for j in range(h[i], n):
            for k in range(j, 0, -1):
                if array[k] <  array[k - h[i]]:
                    break
                else:
                    im = plt.bar(left, height, color="#66cdaa")
                    ims.append(im)
                    array[k], array[k - h[i]] = array[k - h[i]], array[k]
    print(array)
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to clone")
    plt.close()


def main():
    n = parse()
    shellsort(n)

if __name__ == '__main__':
    main()
