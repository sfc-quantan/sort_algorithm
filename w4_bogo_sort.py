# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def lucky_sort(n):
    array = list(range(1, n + 1))
    array2 = array[:]
    random.shuffle(array)
    fig = plt.figure()
    left = range(1, n + 1)
    ims = []
    height = array
    while True:
        if array == array2:
            break
        a = random.randint(0, len(array) - 1)
        b = random.randint(0, len(array) - 1)
        print(a, b)

        array[a], array[b] = array[b], array[a]

        im = plt.bar(left, height, color="#66cdaa")
        ims.append(im)

    ani = animation.ArtistAnimation(fig, ims, interval=5, repeat=False)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = 5
    lucky_sort(n)

if __name__ == "__main__":
    main()
