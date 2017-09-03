# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def lucky_sort(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    while True:
        random.shuffle(array)
        print(array)
        array2 = array[:]
        array2.sort()
        height = array
        im = plt.bar(left, height, color="#66cdaa")
        ims.append(im)
        if array == array2:
            break

    ani = animation.ArtistAnimation(fig, ims, interval=5, repeat=False)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = 6
    lucky_sort(n)

if __name__ == "__main__":
    main()
