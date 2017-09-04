# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse


def combsort(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    height = a
    h = int(n/2)
    count = 1
    for i in range(h,0,-1):
        for j in range(0, n - i):
            if a[j] <= a[j + i]:
                a[j], a[j + i] = a[j + i], a[j]
                
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)

    while not count == 0:
        count = 0
        for k in range(n - 1):
            if a[k] <= a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                count+=1
                im = plt.bar(left, height, color="#66cdaa")
                ims.append(im)
    
    
    
    print(a) 
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    combsort(n)


if __name__ == '__main__':
    main()
