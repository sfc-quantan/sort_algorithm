# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def a_part_of_quicksort(array,dev=0):
    if len(array) ==1:
        return array
    x = int(len(array)/2)
    pivot = array[x]
    print(pivot)
    left, right = 0, 0
    #if not dev == 0:
    array1,array2=array[:dev], array[dev:]

    for k in range(len(array)):
        while True:
            for i in range(len(array) - 1):
                if pivot < array[k][i]:
                    left = i
                    break
            for j in range(len(array) - 1, 0, -1):
                if pivot > array[k][j]:
                    right = j
                    break
            if left < right:
                array[k][left], array[k][right] = array[k][right], array[k][left]
                print(array)
            else:
                # array1,array2 = array[:left], array[left:]
                array = [inner for outer in array for inner in outer]
                break
    return array,left



def quicksort(n):
    array = list(range(0, n))
    random.shuffle(array)
    p = 2
    dev = 0
    while p < n:
        p *= 2
        left = dev
        array,left = a_part_of_quicksort(array,left) 
        print(array)


def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
