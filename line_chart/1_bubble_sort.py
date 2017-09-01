# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def bubblesort(array):
    fig = plt.figure()
    count = 0
    ims=[]
    for i in range(len(array) - 1):
        array2 = array[:]
        for j in range(len(array) - 1):
            im = plt.plot(array)
            ims.append(im)
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

        if array2 == array:
            break
    ani = animation.ArtistAnimation(fig, ims)
    plt.show()


def main():
    a = list(range(10))
    random.shuffle(a)
    bubblesort(a)


if __name__ == '__main__':
    main()
