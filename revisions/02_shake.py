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
    height = a
    reverse = 0
    for i in range(n - 1):
        if reverse == 0:
            for j in range(n - 1):
                if a[j] <= a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    im = plt.bar(left, height, color="#66cadd")
                    ims.append(im)
    
            for j in range(n - 1, 0, -1):
                if a[j - 1] <= a[j]:
                    a[j-1], a[j] = a[j], a[j-1]  
                    im = plt.bar(left, height, color="#66cadd")
                    ims.append(im)
        reverse = 1 if reverse == 0 else 0
        print(a) 
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30, repeat=False)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    bubblesort(n)


if __name__ == '__main__':
    main()
