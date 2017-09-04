# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse


def selectionsort(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []

    for i in range(n - 1):
        mini = a[i]
        for j in range(i, n):
            if mini >= a[j]:
                mini = a[j]
                idx = j

        if not mini == a[i]:
            a[i], a[idx] = a[idx],a[i]
        print(a)

    
    
    
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    selectionsort(n)


if __name__ == '__main__':
    main()
