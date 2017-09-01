# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


def insert_sort(array):
    fig = plt.figure()
    ims = []
    for i in range(1, len(array) + 1):
        print(array)
        if i >= len(array):
            break
        temp = array[i]
        for j in reversed(range(i)):
            im = plt.plot(array)
            ims.append(im)
            if temp > array[j]:
               # temp2 = array[j + 1]
               # array[j + 1] = array[j]
               # array[j] = temp2
               array[j + 1], array[j] = array[j], array[j + 1]

            else:
                array.pop(j + 1)
                array.insert(j + 1, temp)
                break

    ani = animation.ArtistAnimation(fig, ims, repeat_delay=1000)
    plt.show()
    sleep(3)



def main():
    a = list(range(10))
    random.shuffle(a)
    print(insert_sort(a))

if __name__ == '__main__':
    main()
