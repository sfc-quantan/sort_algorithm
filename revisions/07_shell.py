# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse


def shellsort(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    h = [ 7,4,2,1,]
    for i in range(len(h)):
        for j in range(h[i],n):
            for k in range(j, 0 ,-1):
                if a[k - h[i]] < a[k]:
                    a[k-h[i]], a[k] = a[k], a[k-h[i]]
                    height= a
                    im = plt.bar(left, height, color="#66cdaa")
                    ims.append(im)
                else:
                    break
    print(a)
    
    
    
    
    
    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    shellsort(n)


if __name__ == '__main__':
    main()
