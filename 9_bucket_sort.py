# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse

def flatten(nested_list):
    return [e for inner_list in nested_list for e in inner_list]


def bucketsort(n):
    array = list(range(1, 1 + n))
    random.shuffle(array)
    fig = plt.figure()
    height = array
    left = range(1, n + 1)
    ims = []
    bucket = []
    print(array)
    for i in range(n):
        bucket.append([])

    for i in range(n):
        for j in range(1,n + 1):
            if array[i] == j:
                bucket[j-1].append(array[i])


    im = plt.bar(left, height, color="#66cdaa")
    ims.append(im)

    b = flatten(bucket)
    print(b)
    height = b
    im = plt.bar(left, height, color="#66cdaa")
    ims.append(im) 
    ani = animation.ArtistAnimation(fig, ims, interval=600)
    plt.show(block=False)
    input("Enter to close")
    plt.close()






def main():
    n = parse()
    bucketsort(n)

if __name__ == "__main__":
    main()
    

