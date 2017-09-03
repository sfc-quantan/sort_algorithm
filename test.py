# -*-coding: utf-8 -*-
import random


a = list(range(1,21))
x=10
b,c = a[:x],a[x:]
print(b,c)
add =0
for i in range(10):
    add = 0 if add == 1 else 1
    print(add)

print(type(add),len([]))
for i in range(5):
    print(random.randint(1,2))
