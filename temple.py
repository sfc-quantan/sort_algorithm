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
    
    
    
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    ddddddddd(n)


if __name__ == '__main__':
    main()
