# my_random
Python Package

This package provides various methods to generate randomness

--------
Provides
--------
  1. Random Floats & Integer generation function
  2. Random generation of numbers over a gaussian distribution
  3. Choice function - to choose item randomly from a list

-----------------
Available Modules
-----------------
``random_gen.py``        Provides methods like random, ranChoice, uniform, etc <br>
``random_gauss_dist.py`` It gives method to generate random numbers over a gaussian distribution

----------------
random_gen.py -> Python Module
----------------
Pseudo Random Generator

It genrates pseudo random numbers using Linear Congruential Generator function.

Func
-----------------------------
X =    (seed * a + c) mod m<br>
Xn+1 = (Xn * a + c) mod m<br>
a =    multilplier<br>
c =    increment<br>
m =    modulus<br>

PseudoGen(Class)
---------------------------------------
a                multilplier
c                increment
m                modulus

Utility functions
---------------------------------------------------------------------------------
random() ->              Random Numbers Between ``[0, m)`` <br>
uniform() ->             Uniformly distributed floats over ``[0, 1)`` with 4 precision <br>
randChoiceIntRange() ->  Uniformly distributed integer over ``[start, end]`` <br>
randChoice() ->          Random sample from 1-D array or list. <br>

---------------------------
random_gauss.py -> Python Module
---------------------------
Pseudo Random Generator Gauss

It genrates pseudo random numbers over a gaussian distribution.

PseudoGen(Class)
-------------------------------------
a  =              multilplier
c  =              increment
m  =              modulus

Utility functions
---------------------------------------------------------------------------------
std_dis()  ->          Generates Random Numbers over a gaussian distribution 

