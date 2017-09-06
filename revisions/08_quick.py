# -*- coding:utf-8 -*-
import random
from parser import parse


def quicksort(a):
    if len(a) < 1:
        return a
    pivot_num = int(len(a) / 2)
    pivot = a[0]
    left, right = [], []
    
    for i in range(1,len(a)):
        if a[i] < pivot:
            left.append(a[i])
        if a[i] > pivot:
            right.append(a[i])
    print(left,pivot,right)
    left  = quicksort(left)
    right = quicksort(right)

    print(left,pivot,right)
    return left +[pivot] + right
        


def main():

    n = parse()
    a = list(range(1, n + 1))
    random.shuffle(a)
    a = quicksort(a)
    print(a)


if __name__ == "__main__":
    main()
