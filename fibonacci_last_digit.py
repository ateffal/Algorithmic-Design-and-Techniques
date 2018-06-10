# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 08:55:52 2018

@author: TEFFAL AMINE
"""

# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    
    F_i_2 = 0
    F_i_1 = 1
    
    
    for i in range(2,n+1):
        F_i = (F_i_1 + F_i_2) % 10
        
        F_i_2 = F_i_1
        F_i_1 = F_i
        
    

    return F_i

if __name__ == '__main__':
#    input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))


