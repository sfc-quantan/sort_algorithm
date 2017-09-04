# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse


def gnormsort(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    g = 1
    while g < n:
        if a[g - 1] >= a[g]:
             a[g], a[g - 1] = a[g - 1], a[g]
             print(a)
             if g > 1:
                 g-=1
        else:
            g+=1

    print(a)
    
    
    
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    gnormsort(n)


if __name__ == '__main__':
    main()
