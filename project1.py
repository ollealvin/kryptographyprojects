# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:50:32 2018

@author: Olle Alvin
"""
import sys
import numpy as np
import scipy.linalg as linalg
from numpy.linalg import svd as svd
import math

def main(argv):
    print("main")
    #N = argv[0]
    print(argv)

    N = 67591
    L = 30
    F = make_prime_list(L)
    print(F)
    r_list, M = r_generator(F, N, L)
    print(r_list)
    print(M)
    x = nullspace(M)
    print(x)


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
    
    
    M = np.zeros((L,len(F)),dtype='int')
    created_rows = 0
    for j in range(1, L):
        for k in range(1, L+30):
            r = (math.floor(math.sqrt(k*N)) + j)
            r_squared = r**2 % N
            factors = []

            for p in F:
                while r_squared % p == 0 and r_squared !=0:
                    r_squared = r_squared / p
                    factors.append(p)

            if r_squared == 1:
                row = np.zeros(len(F), dtype='int')
                for i in range(len(F)):
                    p = F[i]
                    exponent = factors.count(p)
                    exponent = exponent %2
                    row[i] = exponent
                row_found = False
                for m in range(created_rows):
                    if (np.array_equal(row,M[m,:])):
                        row_found = True
                        
                if not row_found:
                    M[created_rows, :] = row
                    tuples.append((r, factors))
                    created_rows += 1
                    print(created_rows)
                if created_rows == L:
                    return tuples, M

    if len(tuples) != L:
        print("WARNING: The r_generator needs improvement!!!")



def nullspace(A, atol=1e-13, rtol=0):
    A = np.atleast_2d(A)
    u, s, vh = svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    ns = vh[nnz:].conj().T
    return ns

if __name__ == "__main__": main(sys.argv[1:])






