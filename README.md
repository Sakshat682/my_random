# How to use this package?
1. first go to the site_packages directory inside your python, like in my case I have done this <br>```cd C:\Users\<your-user-name>\anaconda3\Lib\site-packages```
2. Then clone this repository at that location using ```git clone https://github.com/Sakshat682/my_random.git```
3. Make sure the name of folder is 'my_random'
4. Now after all this the package is added into your global packages list , so now you can directly import them like: 
```python 
import my_random
# from my_random import *
# from my_random import random_gen
# from my_random.random_gen import PseudoGen
from my_random import PseudoGen as PG
from my_random import random_gauss_dist as rgd

N = 100
print(PG().uniform(N)) # generates random number between [0,1)
print(rgd.std_dis(n,seed,mean,std)) # Generates Random number over a gaussian distribution (mean, std)
```
5. Package Structure is like :
```python
my_random/
├── __init__.py
├── random_gauss_dist.py ── 1) std_dis(n)  # It is a function, def is : std_dis(n,seed=os.getpid()+time.time(),mean=0, std=1) 
└── random_gen.py ── PsedoGen # It is a Class
                        ├── random(n) # function def is: random(self,n,seed=os.getpid()+time.time())
                        ├── uniform(n) # function def is: uniform(self,n,seed=os.getpid()+time.time())
                        └── ranChoiceIntRange(n,start,end) # function def is: ranChoiceIntRange(self,n,seed=os.getpid()+time.time(),start=1,end=100)
                        └── randChoice(n,lt) # function def is: randChoice(self,n,lt,seed) # lt is a list of items
```
----------------------------
# my_random
Python Package

This package provides various methods to generate randomness

Provides
--------
  1. Random Floats & Integer generation function
  2. Random generation of numbers over a gaussian distribution
  3. Choice function - to choose item randomly from a list

Available Modules
-----------------
``random_gen.py``        Provides methods like random, ranChoice, uniform, etc <br>
``random_gauss_dist.py`` It gives method to generate random numbers over a gaussian distribution

----------------
# 1. random_gen.py -> Python Module
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
# 2. random_gauss_dist.py -> Python Module
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

