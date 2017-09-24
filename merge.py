import random
from parser_n import parse

def merge2(a):

    a =[a[i:i+2] for i in range(0,len(a),2)]
    return a
def merge(array):                                   # line1
    mid = len(array)                                # line2
    if mid > 1:                                     # line3
        left = merge(array[:(mid/2)])               # line4
        right = merge(array[(mid/2):])              # line5
        array = []                                  # line6
        while len(left) != 0 and len(right) != 0:   # line7
            if left[0] < right[0]:                  # line8
                array.append(left.pop(0))           # line9
            else:                                   # line10
                array.append(right.pop(0))          # line11
        if len(left) != 0:                          # line12
            array.extend(left)                      # line13
        elif len(right) != 0:                       # line14
            array.extend(right)                     # line15
    return array                                    # line16

def main():
    n = parse()
    a = list(range(1, 1 +n))
    random.shuffle(a)
    a = merge(a)
    print(a)

if __name__ == "__main__":
    main()
