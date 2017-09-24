# -*- coding:utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def shake(a):
    count = 0
    left = 0
    right = len(a)-1
    fig = plt.figure()
    ims = []
    left1 = range(1, len(a) + 1)
    height = a
    for i in range(len(a)):
        temp = 0
        if i % 2 == 0:
            for j in range(left,right):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    temp = j
                    im = plt.bar(left1,height, color="#66cadd")
                    ims.append(im)

                right = temp
        else:
            for j in range(right, left, -1):
                if a[j-1] >  a[j]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                    temp =  j 
                    im = plt.bar(left1, height, color="#66cadd")
                    ims.append(im)
                left = temp
        if left == right:
            break
        print(right,left) 

    
    ani = animation.ArtistAnimation(fig, ims, interval=30, repeat=False)
    plt.show(block=False)
    input("Enter to close")
    plt.close()
    return a


def main():
    n = parse()
    a = list(range(1, n + 1))
    random.shuffle(a)
    a = shake(a)
    print(a)

if __name__ == "__main__":
    main()


