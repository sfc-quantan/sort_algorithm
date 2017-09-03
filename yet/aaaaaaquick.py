# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def a_part_of_quicksort(arrayi,dev):
    x = int(len(array)/2)
    pivot = array[x]
    left, right = 0, 0
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
            # array1, array2 = array[:left], array[left:]
            # array3 = array1,array2
            break
    return array, left



def quicksort(n):
    array = list(range(0, n))
    random.shuffle(array)
    p = 2
    while p < n:
        p *= 2
        array = a_part_of_quicksort(array) 
        print(array)


def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def a_part_of_quicksort(array):
    if len(array)==1 or len(array)==0:
        return array
    x = int(len(array)/2)
    pivot = array[x]
    print(pivot)
    left, right = 0, 0
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
            array1, array2 = array[:left], array[left:]
            # array3 = array1,array2
            break
    return array1, array2 # array3



def quicksort(n):
    array = list(range(0, n))
    random.shuffle(array)
    p = 2
    while p < n:
        p *= 2
        array = a_part_of_quicksort(array) 
        print(array)


def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def a_part_of_quicksort(array):
    if len(array)==1 or len(array)==0:
        return array
    x = int(len(array)/2)
    pivot = array[x]
    print(pivot)
    left, right = 0, 0
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
            array1, array2 = array[:left], array[left:]
            # array3 = array1,array2
            break
    return array1, array2 # array3



def quicksort(n):
    array = list(range(0, n))
    random.shuffle(array)
    p = 2
    while p < n:
        p *= 2
        array = a_part_of_quicksort(array) 
        print(array)


def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
