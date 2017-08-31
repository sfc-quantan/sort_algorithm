# -*- coding: utf-8 -*-
import random


def bubblesort(array):
    count = 0
    for i in range(len(array) - 1):
        array2 = array[:]
        print(count)
        count += 1
        for j in range(len(array) - 1):
            print(array)
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
        if array2 == array:
            break


def main():
    a = list(range(10))
    random.shuffle(a)
    print(bubblesort(a))


if __name__ == '__main__':
    main()
