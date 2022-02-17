"""
Pseudo Random Generator Gauss
=============================

It genrates pseudo random numbers over a gaussian distribution.

================ ======================
PseudoGen(Class)
---------------- ----------------------
a                multilplier
c                increment
m                modulus
================ =======================

==================== =============================================================
Utility functions
-------------------- -------------------------------------------------------------
std_dis()            Generates Random Numbers over a gaussian distribution 
==================== =============================================================

"""

import math
import os
import time
from scipy import special
import numpy as np
from matplotlib import pyplot as plt
from my_random.random_gen import PseudoGen as pg


plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True

# m = pg().__m
# a = pg().__a
# c = pg().__c

def std_dis(n,seed=os.getpid()+time.time(),mean=0, std=1):
    """
    Generates Random number over a gaussian distribution (mean, std)

    You can also set seed to get the same random integer again
    during development phase.

    ``CDF``
    -------
    phi(z)= 1/2(1+erf(z/sqroot(2)))\n
    z= (x-mean)/std\n
    phi(z)= y\n
    z= sqroot(2)*erfinv(2*y +- 1)\n
    x= std*z + mean\n

    ``Parameters``
    --------------
    n : number of elements/numbers to be returned.

    seed : give a number to set as a seed
        Seed make sure you get the same random numbers again
    
    mean : mean of the distribution
        default set to 0

    std : Standard Deviation(sigma) of your distribution
        default set to 1

    ``Returns``
    -----------
    Returns a list of random integers between [start,end].

    ``Examples``
    ------------

    """
    uni_list = pg().uniform(n,seed)
    #  2*y -1 (change range from (0,1) to (-1,1))
    ran_y_list = [round((2*i-1), 4) for i in uni_list]
    std_dis_x_list = []
    for y in ran_y_list:
        if y>=0:
            inp = 2*y - 1
        else:
            inp = 2*y +1
        # inp=y
        if inp<= -1:
            std_dis_x_list.append(mean-4*std)
        elif inp>=1:
            std_dis_x_list.append(mean+4*std)
        else:
            std_dis_x_list.append(round((math.sqrt(2)*std*(special.erfinv(inp))+mean),4))

    return std_dis_x_list

def main():
    seed = int(input("Enter the seed: "))
    n = int(input("Enter the number: "))
    mean = float(input("Enter the mean: "))
    std = float(input("Enter the std: "))

    std_dis_list = std_dis(n,seed,mean,std)
    # print(std_dis_list)
    u=0
    for i in std_dis_list:
        u += i
    u = round(u/n,2)
    print(u)
    count, bins_count = np.histogram(std_dis_list, bins=20)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)

    plt.hist(std_dis_list, bins=20, label='PDF_hist')
    plt.show()
    plt.plot(bins_count[1:], pdf, label="PDF")
    plt.show()
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()