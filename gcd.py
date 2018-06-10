# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:40:28 2018

@author: TEFFAL AMINE
"""

# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    if a == 0:
        return b
   
    if b == 0:
        return a
    
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))