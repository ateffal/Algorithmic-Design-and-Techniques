# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:51:04 2018

@author: TEFFAL AMINE
"""

# Uses python3
import sys
from gcd import *

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    
    # if not found return a*b which is a commun multiple of a and b
    return a*b


def lcm(a, b):
    gcd_ = gcd(a,b)
    return (int(a/gcd_) * b)



if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))