"""
    This tool will create randomly sized files in a psecified diretory for version 1.00.
  Ver: 1.00
    Story:
    - Command-line input determines the directory
    - Directory number at root will be fixed at 1
      - There will be NO sub-directory support
    - A random number of non-sense files will be placed into each directory
  Ver 1.20
    Story:
    - Directory number at root will be 2 or more
      - Two ore more, sub-directories will also be supported
  Ver 1.30
    Story:
    - A random number of directories and depth will be added
      - The number based on command line input
"""

import os, sys
from random import getrandbits
from random import random
#       getrandbits(k) -> x.  Generates an int with k random bits.
#random(...)
#       random() -> x in the interval [0, 1)

def dir_creator(path, d, w):
  d_gen = ""
  w_gen = [a for a in range(1,w)] #1, 2, 3...
  #create binary generator - this may be a separate module
  
  print(w_gen)


dir_creator(" ", 4, 5):
  


def bin_gen(w_gen, length): #define the names of the folders
  
