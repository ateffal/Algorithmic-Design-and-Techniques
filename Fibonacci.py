# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:39:27 2018

@author: TEFFAL AMINE
"""

# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    
    F_i_2 = 0
    F_i_1 = 1
    
    
    for i in range(2,n+1):
        F_i = F_i_1 + F_i_2
        
        F_i_2 = F_i_1
        F_i_1 = F_i
        
    

    return F_i

n = int(input())
print(calc_fib(n))