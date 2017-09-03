# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse


def cyclesort(n):
    array = list(range(1, 1 + n))
    random.shuffle(array)
    fig = plt.figure()
    height = array
    left = range(1, n + 1)
    ims = []
    p = 0
    count = 0
    while not p == n - 1:
        for i in range(p + 1, n):  # 1ではなくp+1であることに気づくのに時間がかかった
            if array[p] < array[i]:
                count += 1
        if count == 0:
            p += 1
        else:
            array[p], array[p + count] = array[p + count], array[p]
            count = 0
            print(array)
            im = plt.bar(left, height, color="#66cdaa")
            ims.append(im)

    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


def main():
    n = parse()
    cyclesort(n)

if __name__ == "__main__":
    main()
