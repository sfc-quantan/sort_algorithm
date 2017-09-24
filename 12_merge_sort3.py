# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from parser_n import parse

def merge(a):
    if len(a) == 1:
        return a
    if len(a) % 2 == 1:
        a = a + []
    temp = []
    lists = []
   ''' for i in range(0,len(a),2):
        for j in range(len(a[0])):
            for k in range(len(a[i + 1])):
                if a[i][j] < a[i + 1][k]:
                    
                    temp.append(a[i][j])
                else:
                    temp.append(a[i + 1][k])
              
        while len(a[i]) > 1 and len(a[i + 1]) > 1:
'''
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a)-j-1):
                if a[i][j] 
            
                

        print(temp)
        lists.append(temp)
        print(lists)
        temp = []

    lists = merge(lists)
    return lists


def mergetsort(n):
    array = list(range(1, 1 + n))
    random.shuffle(array)
    fig = plt.figure()
    height = array
    ims = []
    p = 2
    a = [array[i:i+p] for i in range(0,n,p)]
    print(a) 
    a = merge(a)
    print(a)

    ani = animation.ArtistAnimation(fig, ims, interval=500, repeat=True)
    plt.show(block=False)
    input("Enter to close")
    plt.close()


                   





def main():
    n = parse()
    mergetsort(n)

if __name__ == "__main__":
    main()
    

