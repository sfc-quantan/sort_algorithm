# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse

def bucketsort(n):
    array = list(range(1, 1 + n))
    random.shuffle(array)
    fig = plt.figure()
    height = array
    ims = []
    p = 2
    for i in range(0, n):
        for j in 
        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]




def main():
    n = parse()
    bucketsort(n)

if __name__ == "__main__":
    main()
    

