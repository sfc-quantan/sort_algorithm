# -*- coding: utf-8 -*-


def buublesort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            print(array)
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def main():
    a = [88, 11, 55, 22, 100, 33, 99, 77, 44, 66]
    print(buublesort(a))


if __name__ == '__main__':
    main()
