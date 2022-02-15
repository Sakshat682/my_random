"""
My Random
=========

This package provides various methods to generate randomness

--------
Provides
--------
  1. Random Floats & Integer generation function
  2. Random generation of numbers over a gaussian distribution
  3. Choice function - to choose item randomly from a list

-----------------
Available Modules
------------------------ -----------------------------------------------------------------------
``random_gen.py``        Provides methods like random, ranChoice, uniform, etc 
``random_gauss_dist.py`` It gives method to generate random numbers over a gaussian distribution
======================== =======================================================================

"""
# import random_gen
from my_random.random_gen import PseudoGen
# import random_gauss_dist
__all__ = ["random_gen","random_gauss_dist"]