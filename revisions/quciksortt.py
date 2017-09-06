# -*- coding:utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def randomarray():
    n = parse()
    a = list(range(1, n + 1))
    random.shuffle(a) 
    return a

def quicksort(a):
    
    if len(a) <= 1:
        return a
    pivot_num = int(len(a)/2)
    pivot = a[0]
    left,right =[],[]

    for i in range(1, len(a)):
        if a[i] <= pivot:
            left.append(a[i])
            
        else:
            right.append(a[i])

    left = quicksort(left)
    right = quicksort(right)
    return left + [pivot]  + right

def main():
    fig = plt.figure()
    ims = []
    a = randomarray()
    print(a)
    left = range(1, len(a) + 1)
    height = a
    im = plt.bar(left,height, color="#66cdaa")
    ims.append(im)
    a = quicksort(a)
    print(a)
    height = a
    im = plt.bar(left,height, color="#66cdaa")
    ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=1000)
    plt.show(block=False)
    input("Enter to close")
    plt.close()



if __name__ == "__main__":
    main()



