# -*- coding: utf-8 -*-
import random


def insert_sort(array):
    for i in range(1, len(array) + 1):
        print(array)
        if i >= len(array):
            break
        temp = array[i]
        for j in reversed(range(i)):
            if temp < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
            else:
                array.pop(j + 1)
                array.insert(j + 1, temp)
                break


def main():
    a = list(range(10))
    random.shuffle(a)
    print(insert_sort(a))

if __name__ == '__main__':
    main()
