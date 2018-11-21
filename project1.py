# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:50:32 2018

@author: Olle Alvin
"""
import sys
import numpy as np
import math
import time

def main():

    N = 145968946107052219367611
    
    L = 500                             #500 works well for large numbers. 
    num_primes = L-10                   #We want a factor base smaller than L.
    
    F = make_prime_list(num_primes)     #Make the factor base.
    
    r_list, M = r_generator(F, N, L)    #Generate numbers, for which the 
                                        #squares are factored by our factor 
                                        #base.
    
    f = open("input.txt", "w")          #Write the binary matrix to a file.
    f.write("%d %d" % (L, len(F)))
    for i in range(L):
        f.write("\n")
        for j in range(len(F)):
            f.write("%d" % M[i,j])
            if j != len(F):
                f.write(" ")
                
    f.close()
    
    #Prompt the user to run GaussBin.exe
    input("Run GaussBin and ress the <ENTER> key to continue...")
    
    #Check solutions
    with open("output.txt") as file:
        
        skipped_first_row = False
        for line in file.readlines():
            factor_dict = {}
            if not skipped_first_row:
                skipped_first_row = True
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
                        if j not in factor_dict:
                            factor_dict[j] = 1
                        else:
                            factor_dict[j] = factor_dict[j] + 1
            
            for k in factor_dict:
                factor_product = factor_product * k**(factor_dict[k]>>1)
                
            v = factor_product - r_product
            v = int(v)
            v = v%N
            if math.gcd(v, N) != 1 and math.gcd(v, N) != N:
                p = math.gcd(v,N)
                q = math.floor(N/p)
                print("Found solution: %d = %d * %d" %(N, p, q))
                return
        print("No solutions")
    


def make_prime_list(num_primes):
    """
    Makes a list of prime numbers with num_primes primes.
    """
    prime_list = []
    prime_list.append(2)
    i = 3
    while len(prime_list) <  num_primes:
        is_prime = True
        for j in prime_list:
            if i % j == 0:
                is_prime=False

        if is_prime:
            prime_list.append(i)
        i += 1

    return prime_list

def r_generator(F, N, L):
    """
    Generates numbers r of the given form, until L numbers can be returned
    that factor over F.
    Returns a list of  L tuples, the first item in the tuple being r and the 
    second being the prime factors of r^2 mod N. 
    Also constructs and returns the binary matrix.
    """
    start = time.clock()
    tuples = []
    sum = 2;
    MAX_SUM = 10000000;
    M = np.zeros((L,len(F)),dtype='int')
    created_rows = 0
    numbers_tested = 0;
    while sum < MAX_SUM:
        for k in range(1,sum-1):
            j = sum-k
            r = (math.floor(math.sqrt(k*N)) + j)
            r_squared = (r**2) % N
            factors = []
            numbers_tested += 1

            for p in F:
                while r_squared % p == 0 and r_squared !=0:
                    r_squared = r_squared / p
                    factors.append(p)
                if r_squared == 1:
                    break

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
                if created_rows == L:
                    stop = time.clock()
                    print("Finished computing numbers factored by our " \
                          "factor base, tested %d numbers, time: %f" 
                          % (numbers_tested, stop-start) )
                    return tuples, M
            
        sum += 1
        
    if sum == MAX_SUM:
        print("Tried %d numbers but did not find enough!" %(MAX_SUM))
        

if __name__ == "__main__": main()






