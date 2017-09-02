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
    ims = []
    for i in range(len(array) - 1):
        array2 = array[:]
        for j in range(len(array) - 1):
            print(array)
            height = array
            im = plt.bar(left, height, color="#66cdaa")
            ims.append(im)
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

        if array2 == array:
            break
    ani = animation.ArtistAnimation(fig, ims)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    bubblesort(n)


if __name__ == '__main__':
    main()
