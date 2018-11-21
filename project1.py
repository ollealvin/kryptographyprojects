# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:50:32 2018

@author: Olle Alvin
"""
import sys
import numpy as np
import math
import time

def main(argv):
    #N = argv[0]
    print(argv)

    N = 145968946107052219367611
    #N = 10967535067
    #N = 16637
    #N = 3205837387 # 46819 · 68473
    #N = 392742364277 #this number does not work.
    L = 500
    num_primes = L-10
    F = make_prime_list(num_primes)
    r_list, M = r_generator(F, N, L)
    f = open("input.txt", "w")
    f.write("%d %d" % (L, len(F)))
    
    for i in range(L):
        f.write("\n")
        for j in range(len(F)):
            f.write("%d" % M[i,j])
            if j != len(F):
                f.write(" ")
                
    f.close()
    print("pause");
    programPause = input("Run GaussBin and ress the <ENTER> key to continue...")
    print("unpause")
    
    #Check solutions
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
                        #factor_product *= j
                        if j not in factor_dict:
                            factor_dict[j] = 1
                        else:
                            factor_dict[j] = factor_dict[j] + 1
            
            for k in factor_dict:
                if factor_dict[k] % 2 != 0:
                    print("ERROR!!!!")
                factor_product = factor_product * k**(factor_dict[k]>>1)
                #factor_product = factor_product % N
            if r_product**2 %N != factor_product**2 %N:
                print("wrong!")
            v = factor_product - r_product
            v = math.floor(v)
            v = v%N
            print(".",end='')
            if math.gcd(v, N) != 1 and math.gcd(v, N) != N:
                p = math.gcd(v,N)
                q = math.floor(N/p)
                print(p,q)
                return
                break
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
    Returns a list of  L tuples, the first item in the tuple being r and the second
    being the prime factors of r^2 mod N.
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
                    print("Added row", created_rows, r,k,j)
                if created_rows == L:
                    stop = time.clock()
                    print("Finished computing numbers factored by our factor base, tested %d numbers, time: %f" % (numbers_tested, stop-start) )
                    return tuples, M
            
        sum += 1
        
    if sum == MAX_SUM:
        print("Tried %d numbers but did not find enough!" %(MAX_SUM))
    if len(tuples) != L:
        print("WARNING: The r_generator needs improvement!!!", len(tuples))
        

if __name__ == "__main__": main(sys.argv[1:])






