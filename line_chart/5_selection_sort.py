# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


def selection_sort(array):
    idx = 0
    fig = plt.figure()
    ims = []
    for i in range(len(array)):
        print(array)
        temp = array[i]
        for j in range(i+1,len(array)):
            if temp < array[j]:
                temp = array[j]
                idx = j
                im = plt.plot(array)
                ims.append(im)
        if not temp == array[i]:
            array[idx] = array[i]
            array[i]=temp
            im = plt.plot(array)
            ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, repeat_delay=1000 )
    plt.show()


def main():
    a = list(range(10))
    random.shuffle(a)
    selection_sort(a)



if __name__ == '__main__':
    main()

