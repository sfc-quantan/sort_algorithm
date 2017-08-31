# -*- coding: utf-8 -*-
import random

def selection_sort(array):
    idx = 0
    for i in range(len(array)):
        print(array)
        temp = array[i]
        for j in range(i+1,len(array)):
            if temp < array[j]:
                temp = array[j]
                idx = j
        if not temp == array[i]:
            array[idx] = array[i]
            array[i]=temp



def main():
    a = list(range(10))
    random.shuffle(a)
    print(selection_sort(a))


if __name__ == '__main__':
    main()

