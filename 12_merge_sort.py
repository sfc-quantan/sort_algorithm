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
    while p/2 <=  n:
        a= [array[i:i+p] for i in range(0,n,p)]

        for i in range(len(a)):
            for j in range(len(a[i]) - 1):
                for k in range(len(a[i]) - 1):
                    if a[i][k] < a[i][k + 1]:
                        a[i][k], a[i][k + 1] = a[i][k + 1], a[i][k]
        p*=2
        temp = []
        for b in range(len(a)):
            temp.extend(a[b])
        
        left = range(1, n+1)
        height = temp
        
        im = plt.bar(left, height, color="#66cdaa")
        ims.append(im)
        a = temp
        print(a)

    ani = animation.ArtistAnimation(fig, ims, interval=500, repeat=True)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


                   





def main():
    n = parse()
    bucketsort(n)

if __name__ == "__main__":
    main()
    

