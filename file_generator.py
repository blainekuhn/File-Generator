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
from time import sleep

def file_maker(path, d_gen, w_gen, deep):
  import string, random
  dir_dict= {}
  file_list = []
  word = ""
  dirname = ""
  alphabet = string.ascii_letters[0:52] + string.digits #+ string.punctuation
  MB = 1024*1024 # 1MB

  while (deep +1) > 0:
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
    for f in dir_dict:
      p = os.path.join(path, f)
      print("This is p %s" % p)
      os.mkdir(p)
      f_list = dir_dict[f]
      for file in f_list:
        #print("FILE %s" % file)
        #print("this is file %s" % file)
        current_file = os.path.join(p,file)
        with open(current_file, 'wb') as b:
          b.write(os.urandom(MB))
#        dir_creator(p, d_gen, w_gen, deep)
      if (deep+1) > 0:
        file_maker(p, d_gen, w_gen, deep-1)
    return(dir_dict)


file_maker("/Users/blainekuhn/Git/Python/File-Generator", 2, 10, 3)





