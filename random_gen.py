"""
Pseudo Random Generator
=======================

It genrates pseudo random numbers using Linear Congruential Generator function.

===== ======================
Func
----- ----------------------
X     (seed * a + c) mod m
Xn+1  (Xn * a + c) mod m
a     multilplier
c     increment
m     modulus
===== =======================

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
random()               Random Numbers Between ``[0, m)``
uniform()              Uniformly distributed floats over ``[0, 1)`` with 4 precision
randChoiceIntRange()   Uniformly distributed integer over ``[start, end]``
randChoice()           Random sample from 1-D array or list.
==================== =============================================================

"""

import math
import os
import time


class PseudoGen:
    """
    Class to generate Random Numbers.
    Consist of 4 functions random, uniform, ranChoiceIntRange, & ranChoice.
    """
    __m = 2**32
    __a = 347159
    __c = 8231
    def __init__(self):
        pass

    def random(self,n,seed=os.getpid()+time.time()):
        """
        Generates Random Numbers between [0,m), where m is the modulo number.

        You can also set seed to get the same random numbers again
        during development phase.

        ``Parameters``
        --------------
        n : number of elements/numbers to be returned.

        seed : give a number to set as a seed
            Seed make sure you get the same random numbers again

        ``Returns``
        -----------
        Returns a list of random genrated numbers between [0,m).

        """
        first = ((seed*self.__a + self.__c) % self.__m)
        next = first
        ranList = []
        for _ in range(n):
            ranList.append(next)
            next = ((next*self.__a + self.__c) % self.__m)
        return ranList

    def uniform(self,n,seed=os.getpid()+time.time()):
        """
        Generates Random Numbers between [0,1).

        You can also set seed to get the same random numbers again
        during development phase.

        ``Parameters``
        --------------
        n : number of elements/numbers to be returned.

        seed : give a number to set as a seed
            Seed make sure you get the same random numbers again

        ``Returns``
        -----------
        Returns a list of uniformly distributed random numbers between [0,1).

        """
        ranList = self.random(n,seed)
        uniList=[]
        for i in ranList:
            uniList.append(round(i/self.__m, 4))
        return uniList

    def ranChoiceIntRange(self,n,seed=os.getpid()+time.time(),start=1,end=100):
        """
        Generates Random Integer between [start,end], where m is the modulo number.

        You can also set seed to get the same random integer again
        during development phase.

        ``Parameters``
        ----------
        n : number of elements/numbers to be returned.

        seed : give a number to set as a seed
            Seed make sure you get the same random numbers again
        
        start : Integer to start with
            default set to 1

        end : Integer to end with
            default set to 100

        ``Returns``
        -----------
        Returns a list of random integers between [start,end].

        ``Examples``
        ------------
        for dice roll

        """       
        range = end - start
        uniList = self.uniform(n,seed)
        ranChoiceList = []
        for i in uniList:
            ranChoiceList.append(round(i*range) + start)
        return ranChoiceList

    def randChoice(self,n,lt,seed):
        """
        Gives random items from the given list of items

        You can also set seed to get the same random numbers again
        during development phase.

        ``Parameters``
        --------------
        n : number of elements/numbers to be returned.

        lt : Provide a list of items

        seed : give a number to set as a seed
            Seed make sure you get the same random numbers again

        ``Returns``
        -----------
        Returns a list of uniformly distributed random items  

        ``Examples``
        ------------

        """
        ran_list = self.ranChoiceIntRange(n,seed,1,len(lt))
        ran_choice = [lt[i-1] for i in ran_list]
        return ran_choice

def main():
    rn = PseudoGen()
    seed = int(input("Enter the seed: "))
    n = int(input("Enter the number: "))
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the last number: "))
    lt = ['SJ','Asher','Logan','Prakhar','sinu','ram','shyam']
    random_list = rn.random(n,seed)
    print(random_list)
    uni_list = rn.uniform(n,seed) 
    print(uni_list)
    ran_int_choice_list = rn.ranChoiceIntRange(n,seed,start,end) 
    print(ran_int_choice_list)
    ran_choice = rn.randChoice(n,lt,seed)
    print(ran_choice)

if __name__ == '__main__':
    main()