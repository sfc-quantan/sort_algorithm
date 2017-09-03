# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def strandsort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    t_list = []
    s_list = []
    pop = []

    while len(array):
        temp = array[0]
        pop.append(array[0])
        t_list.append(array[0])
        for i in range(1, len(array)):
            if temp > array[i]:
                temp = array[i]
                t_list.append(array[i])
                pop.append(temp)
                print("t:", t_list)
        for l in range(len(pop)):
            array.remove(pop[l])

        s_list.extend(t_list)
        height = s_list
        left = range(1, len(s_list) + 1)
        for i in range(len(s_list) - 1):
            for j in range(len(s_list) - 1):
                if s_list[j] < s_list[j + 1]:
                    s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
                    im = plt.bar(left, height, color="#66cdaa")
                    ims.append(im)

        t_list = []
        pop = []
        print("s:", s_list)
        print("a:", array)

    ani = animation.ArtistAnimation(fig, ims, interval=30, repeat=False)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    strandsort(n)


if __name__ == "__main__":
    main()
