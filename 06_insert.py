# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse


def insertsort(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    height = a

    for i in range(1,n):
        for j in range(i, 0, -1):
            if a[j-1] <= a[j]:
                a[j-1],a[j] = a[j], a[j-1]
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
        print(a)

            

    
    
    
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    insertsort(n)


if __name__ == '__main__':
    main()
