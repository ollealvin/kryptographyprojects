# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:24:21 2018

@author: Olle Alvin
"""

import sys
import numpy as np
import math
import os

def main():
    N = 67591
    L = 30
    F = make_prime_list(L)
    with open("output.txt") as file:
        line = file.readline
        counter = 1
        while line:
            row_s = line.split("\\s+")
            for i in range(len(row_s)):
                
            
def make_prime_list(L):
    prime_list = []
    prime_list.append(2)
    for i in range(3,L):
        is_prime = True
        for j in prime_list:
            if i % j == 0:
                is_prime=False

        if is_prime:
            prime_list.append(i)

    return prime_list
            
if __name__ == "__main__": main()
        