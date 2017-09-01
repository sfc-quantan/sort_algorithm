# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def quicksort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    if not n % 2 == 0:
        array.append(-1000000)

    count = 0
    for j in range(1,n):
        if 2**j < n:
            print(2**j)
            count+=1
        else:
            count+=1
            break
    


    for i in range(0,n,2):
        print(array)
        if array[j] < array[j + 1]:
             array[j + 1], array[j] = array[j], array[j + 1]



def main():
    n = parse()
    quicksort(n)

if __name__ == '__main__':
    main()
