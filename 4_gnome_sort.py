# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  parser_n import parse

def gnomesort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    g = 1
    while g < n:
        print(array)
        height = array
        im = plt.bar(left, height, color="#66cdaa")
        ims.append(im)
        if array[g - 1] > array[g]:
            array[g], array[g - 1] = array[g - 1], array[g]
            if g > 1:
                g -= 1
        else:
            g += 1
    ani = animation.ArtistAnimation(fig, ims)
    plt.show(block=False)
    input("Enter to close")
    plt.close()




def main():
    n = parse()
    gnomesort(n)

if __name__ == '__main__':
    main()
