# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser import parse
import  numpy  as np

def bubblesort(n):
    a = np.random.randint(0, 400, n)
    a = list(range(1,n + 1))
    random.shuffle(a)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    height = a

    for i in range(n):
        for j in range(n - i - 1):
            if a[j] <= a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                #im = plt.bar(left, height, color="#66cdaa")
                #ims.append(im)
    print(a)
    
    
    
    
    
    #ani = animation.ArtistAnimation(fig, ims, interval=30, repeat=False)
    #plt.show(block=False)
    #input("Enter to close")
    #plt.close()


def main():
    n = parse()
    bubblesort(n)


if __name__ == '__main__':
    main()
