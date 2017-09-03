# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse

def flatten(nested_list):
    return [e for inner_list in nested_list for e in inner_list]

def radixsort(n):
    radix = [[], [], [], [], [], [], [], [], [], []]
    array = list(range(1, n + 1))
    array2 = array[:]
    random.shuffle(array)
    keta = 10
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []

    for i in range(keta):
        for l in range(len(array)):
            if i == 0:
                a = int(array[l] % 10)
            else:
                a = array[l]
                for re in range(i):
                    a=int(a/10)
                a=int(a%10)
            for j in range(10):
                if a == j:
                    radix[j].append(array[l])

        height = array
        im = plt.bar(left, height, color="#66cdaa")
        ims.append(im)
        r = flatten(radix)
        array = r[:]
        radix = [[], [], [], [], [], [], [], [], [], []]
        print(r)
        if array2 == array:
            break

    height = array
    im = plt.bar(left, height, color="#66cdaa")
    ims.append(im)           
    ani = animation.ArtistAnimation(fig, ims, interval=550)
    plt.show(block=False)
    input("inter to close")
    plt.close()


def main():
    n = parse()
    radixsort(n)


if __name__ == "__main__":
    main()
