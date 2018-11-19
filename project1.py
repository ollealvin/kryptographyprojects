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
import os
import subprocess

def main(argv):
    haveSolutions = False;
    #N = argv[0]
    print(argv)

    N = 145968946107052219367611
    L = 500
    F = make_prime_list(L)
    r_list, M = r_generator(F, N, L)
    f = open("input.txt", "w")
    f.write("%d %d" % (L, len(F)))
    
    if not haveSolutions:
        for i in range(L):
            f.write("\n")
            for j in range(len(F)):
                f.write("%d" % M[i,j])
                if j != len(F):
                    f.write(" ")
                
        f.close
    else:
        with open("output.txt") as file:
            
            counter = 1
            for line in file.readlines():
                factor_dict = {}
                if counter == 1:
                    counter += 1
                    continue
                row_s = line.strip().split(" ")
                r_product = 1
                factor_product = 1
                factor_dict= {}
                for i in range(len(row_s)): 
                    if row_s[i] == '1':
                        r_product *= r_list[i][0]
                        r_product = r_product % N
                        for j in r_list[i][1]:
                            factor_product *= j
                            if j not in factor_dict:
                                factor_dict[j] = 1
                            else:
                                factor_dict[j] = factor_dict[j] + 1
                
                for k in factor_dict:
                    if factor_dict[k] % 2 != 0:
                        print("ERROR!!!!")
                    factor_product = factor_product * k**(factor_dict[k]/2)
                    factor_product = factor_product % N
                v = factor_product - r_product
                v = math.floor(v)
                v = v%N
                if math.gcd(v, N) != 1:
                    p = math.gcd(v,N)
                    q = math.floor(N/p)
                    print(p,q)
                    break
                        
                        
#    f_out = open("output.txt", "w")
#    f_out.close
    #if os.path.isfile("C:/Users/Olle/Documents/GitHub/kryptographyprojects/GaussBin.exe"):
     #   print("is a file!")
        
    #args = "C:/Users/Olle/Documents/GitHub/kryptographyprojects/GaussBin.exe input.txt output.txt"
    #os.system("C:/Users/Olle/Documents/GitHub/kryptographyprojects/GaussBin.exe input.txt output.txt")
    #subprocess.run(args)
    
    
#    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
#    args = "GaussBin.exe " + "input.txt " + "input.txt"
#    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
#    
#    #os.system("GaussBin.exe input.txt output.txt")
        
    


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
    for j in range(1, N):
        for k in range(1, L + math.floor(L/2)):
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
                    print("Added row", created_rows)
                if created_rows == L:
                    return tuples, M

    if len(tuples) != L:
        print("WARNING: The r_generator needs improvement!!!", len(tuples))
        


if __name__ == "__main__": main(sys.argv[1:])






