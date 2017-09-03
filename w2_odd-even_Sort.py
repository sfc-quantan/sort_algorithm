# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def oddevensort(n):
    odd = 0
    array = list(range(1,n + 1))
    random.shuffle(array)
    fig = plt.figure()
    ims = []
    left = range(1, n + 1)
    height = array

    for i in range(n - 1):
        for j in range(odd, n - 1 - odd):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
                print(array)

        odd = 1 if odd == 0 else 0

    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    oddevensort(n)

if __name__ == "__main__":
    main()
