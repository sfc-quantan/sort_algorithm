# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse


def bubblesort(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []

    for i in range(n - 1):
        for j in range(n - 1):
            if a[j] <= a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
    
    
    
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    gn(n)


if __name__ == '__main__':
    main()
