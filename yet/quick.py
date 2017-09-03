# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def a_part_of_quicksort(array):
    x = int(len(array)/2)
    pivot = array[x]
    print(pivot)
    left, right = 0, 0
    for i in range(5):
        for i in range(len(array) - 1):
            if pivot <=  array[i]:
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
            array1, array2 = array[:left], array[left:]
            # array3 = array1,array2
            a_part_of_quicksort(array1)
            a_part_of_quicksort(array2)

    
            #break


def a_part_of_quicksort2(array,dev):
    if len(array) == 1:
        return array

    array1,array2 = array[:dev], array[dev:]
    # x1, x2 = int(len(array1)), int(len(array2))
    # pivot1,pivot2  = array1[x1],array[x2]
    # print(pivot1,pivot2)
    a_part_of_quicksort(array1)
    a_part_of_quicksort(array2)



def quicksort(n):
    array = list(range(0, n))
    random.shuffle(array)
    a_part_of_quicksort(array)


def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
