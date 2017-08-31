# -*- coding: utf-8 -*-

import random


def insert_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        for j in reversed(range(i+1)):
            print(i,j)
            if temp > array[j]:



            

def main():
    a =list(range(10))
    random.shuffle(a)
    print(insert_sort(a))


if __name__ == '__main__':
    main()
