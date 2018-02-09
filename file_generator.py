"""
    This tool will create randomly sized files in a psecified diretory for version 1.00.
  Ver: 1.00
    Story:
    - Command-line input determines the directory
    - Directory number at root will be fixed at 1
      - There will be NO sub-directory support
    - A user set number of non-sense binary files will be placed into each directory
  Ver 1.20
    Story:
    - Directory number at root will be 2 or more
      - Two ore more, sub-directories will also be supported
  Ver 1.30
    Story:
    - A random number of directories and depth will be added
      - The number based on command line input
"""

import os, sys, random, string
from random import getrandbits
from random import random, randint


def dir_creator(path, d, w):
  d_gen = d #will eventually = [a for a in range(1, d)]
  w_gen = w
  dir_dict = name_gen(d_gen, w_gen)
  file_maker(path, dir_dict) #will change when path is introduced


def file_maker(path, f_dict):
  MB = 1024*1024 # 1MB
  alphabet = string.ascii_letters[0:52] + string.digits 
  count = 0
  for f in f_dict:
    os.mkdir(f)
    f_list = f_dict[f]
    for file in f_list:
      print("this is file %s" % file)
      with open(os.path.join(f,file), 'wb') as b:
        b.write(os.urandom(alphabet))


def name_gen(d_gen, w_gen): #define the names of the folders
  import string, random
  dir_dict= {}
  file_list = []
  word = ""
  dirname = ""
  alphabet = string.ascii_letters[0:52] + string.digits #+ string.punctuation
  for a in range(d_gen):
    for x in random.sample(alphabet,random.randint(8, 15)):
      dirname += x
    for b in range(w_gen):
      for x in random.sample(alphabet,random.randint(8, 15)):
        word += x
      file_list.insert(b,word)
      word = ""
    dir_dict[dirname] = file_list
    file_list = []
    dirname = ""
 
  return(dir_dict)


dir_creator("sdf", 2, 10)





