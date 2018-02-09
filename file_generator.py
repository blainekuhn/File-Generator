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


def dir_creator(path, d, w, deep):
  d_gen = d #will eventually = [a for a in range(1, d)]
  w_gen = w
 # print("In 10 sconds %s MB of data will be generated on the file system." % (d*w))
 # sleep(10)
  dir_dict = name_gen(d_gen, w_gen)
  file_maker(path, dir_dict) #will change when path is introduced


def file_maker(path, f_dict):
  MB = 1024*1024 # 1MB
  count = 0
  p = ""
  for f in f_dict:
    p = os.path.join(path, f)
    print("This is p %s" % p)
    os.mkdir(p)
    f_list = f_dict[f]
    for file in f_list:
      #print("this is file %s" % file)
      with open(os.path.join(p,file), 'wb') as b:
        b.write(os.urandom(MB))


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


dir_creator("/Users/blainekuhn/Git/Python/md5_checker", 2, 10, 3)





