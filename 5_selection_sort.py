# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def selection_sort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    idx = 0
    left = range(1, len(array) + 1)
    fig = plt.figure()
    ims = []
    for i in range(len(array)):
        print(array)
        temp = array[i]
        for j in range(i + 1, len(array)):
            if temp < array[j]:
                temp = array[j]
                idx = j
                height = array
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
        if not temp == array[i]:
            array[idx] = array[i]
            array[i] = temp
            im = plt.bar(left, height, color="#66cdaa")
            ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, repeat_delay=1000)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    selection_sort(n)


if __name__ == '__main__':
    main()
