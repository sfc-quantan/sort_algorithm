# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def insert_sort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    ims = []
    left = range(1, len(array) + 1)
    for i in range(1, len(array) + 1):
        if i >= len(array):
            break
        temp = array[i]
        for j in reversed(range(i)):
            height = array
            print(array)
            im = plt.bar(left, height, color="#66cdaa")
            ims.append(im)
            if temp > array[j]:
                # temp2 = array[j + 1]
                # array[j + 1] = array[j]
                # array[j] = temp2
                array[j + 1], array[j] = array[j], array[j + 1]

            else:
               # array.pop(j + 1)
               # array.insert(j + 1, temp)
                break

    ani = animation.ArtistAnimation(fig, ims, repeat_delay=1000)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    insert_sort(n)


if __name__ == '__main__':
    main()
