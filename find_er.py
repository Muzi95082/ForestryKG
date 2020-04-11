# coding:utf8
import codecs
import sys
import pandas as pd
import numpy as np
from collections import deque
import pdb

with open('train.txt', 'r', 'utf-8') as tfc:
    for lines in tfc:
        line = lines.split()
        try:
            index1 = line[3].index(line[0])
            position1 = []
            index2 = line[3].index(line[1])
            position2 = []
            print(enumerate(line[3]))
        except IOError:
            print(line)