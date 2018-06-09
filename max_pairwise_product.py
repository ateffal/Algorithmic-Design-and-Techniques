# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:45:57 2018

@author: TEFFAL AMINE
"""

# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

second_biggest = 0
biggest = 0

for i in range(0, n):
    print('biggest = ', biggest)
    print('second_biggest = ', second_biggest)
    if a[i] > biggest :
        second_biggest = biggest
        biggest = a[i]
    else:
        if a[i] > second_biggest:
            second_biggest = a[i]

        
                
print(biggest*second_biggest)

