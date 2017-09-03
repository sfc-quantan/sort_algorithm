# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse

def stoogesort(n):
    array = list(range(1, n+1))
    random.shuffle(array)

    if n < 3:
        if array[0] < array[1]:
            array[0], array[1] = array[1], array[0] 
    else:
        
        p = int(n* 2 / 3)
        print(p)
        array2 = list(range(1, n + 1))
        while True:
            print(array)
            if array[0] < array[p]:
                array[0], array[p] = array[p], array[0]
            if array[p] < array[-1]:
                array[p], array[-1] = array[-1], array[p]
            if array[0] < array[p]:
                array[0], array[p] = array[p], array[0]
            if array == array2:
                break

def main():
    n = parse()
    stoogesort(n)

if __name__ == "__main__":
    main()


    

