# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:50:32 2018

@author: Olle Alvin
"""
import sys
import numpy as np
import math

def main(argv):
    print("main")
    #N = argv[0]
    print(argv)
    
    N = 67591
    L = 30
    F = make_prime_list(L)
    print(F)
    r_list = r_generator(F, L, N)
    print(r_list)


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

def r_generator(F, N, L):
    """
    GEenerates numbers r of the given form, until L numbers can be returned
    that factor over F. 
    Returns a list of  L tuples, the first item in the tuple being r and the second7
    being the factors of r^2 mod N.
    """ 
    tuples = []
    
    for j in range(1, L):
        for k in range(1, L + 50):
            r = (math.floor(math.sqrt(k*N)) + j)
            r_squared = r**2 % N
            factors = []
            
            for p in F:
                while r_squared % p == 0:
                    r_squared = r_squared / p
                    factors.append(p)
                    
            if r_squared == 1:
                tuples.append((r, factors))
                
            if len(tuples) == L:
                return tuples
                    
                    
                    
#                    if r_squared % p == 0:
#                    r_squared = r_squared/p
#                    factors.append(p)
#                    if r_squared == 1:
#                        tuples.append((r, factors))
#                        break
#            
#            for p in F: 
#                if r_squared % p == 0:
#                    r_squared = r_squared/p
#                    factors.append(p)
#                    if r_squared == 1:
#                        tuples.append((r, factors))
#                        break
#            if len(tuples) == L:
#                return tuples
            
    if len(tuples) != L:
        print("WARNING: The r_generator needs improvement!!!")
                        
                

if __name__ == "__main__": main(sys.argv[1:])






