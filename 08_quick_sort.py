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
    print("a:",a)    
    if len(a) <= 1:
        print("return :",a)
        return a
    pivot_num = int(len(a)/2)
    pivot = a[pivot_num]
    left,right =[],[]

    for i in range(len(a)):
        if a[i] < pivot:
            left.append(a[i])
            
        elif a[i] > pivot:
            right.append(a[i])
        else:
            e = [pivot]

    # print(left,pivot,right)
    print("befor",left,e,right)
    left = quicksort(left)
    right = quicksort(right)
    print("after",left,e,right)
    return left + e + right

def main():
    fig = plt.figure()
    ims = []
    a = randomarray()
    left = range(1, len(a) + 1)
    height = a
    im = plt.bar(left,height, color="#66cdaa")
    ims.append(im)
    a = quicksort(a)
    height = a
    im = plt.bar(left,height, color="#66cdaa")
    ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=1000)
    plt.show(block=False)
    input("Enter to close")
    plt.close()

    print(a)


if __name__ == "__main__":
    main()



