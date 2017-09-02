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
    while True:
        for i in range(len(array) -1):
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
            break
    return array1,array2
    

def quicksort(n):
    array = list(range(0, n))
    random.shuffle(array)
    array1,array2 = a_part_of_quicksort(array)
    print(array1,array2)
        


def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
