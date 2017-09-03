# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def selectionsort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    left = range(1, n + 1)
    fig = plt.figure()
    ims = []
    idx = 0
    height = array
    for i in range(n):
        temp = array[i]
        for j in range(i, n):
            print(array)
            if temp < array[j]:
                temp = array[j]
                idx = j
        if not temp == array[i]:
            array[i], array[idx] = temp, array[i]
            im = plt.bar(left, height, color="#66cdaa")
            ims.append(im)

    ani = animation.ArtistAnimation(fig, ims, interval=30, repeat=True)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    selectionsort(n)

if __name__ == "__main__":
    main()
