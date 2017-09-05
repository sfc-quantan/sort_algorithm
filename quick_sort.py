# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def quicksort(array, left, right):
    x = int(len(array)/2)
    pivot = array[x]
    while True:
        for i in range(len(array) - 1):
            if pivot < array[i]:
                left = i
                break
        for j in range(len(array) - 1, 0, -1):
            if pivot > array[j]:
                right = j
                break
        if left < right:
            array[left], array[right] = array[right], array[left]
            print(array)
        else:
            array = array[:left], array[left:]
            # array3 = array1,array2
            break
    return array


def main():
    n = parse()
    array = list(range(0,n))
    random.shuffle(array)
    left, right =0, 0
    array=quicksort(array, left, right)
    print(array)


if __name__ == '__main__':
    main()
