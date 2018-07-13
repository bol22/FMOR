# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:34:32 2018

@author: liub725
"""
import re
import math
import sys
import matplotlib.pyplot as plt
import networkx as nx
#arg = sys.argv[1]
#inf = open(arg,'r')
#inf=open('test.glm','r')
##-----------------------
## Pull Model Into Memory
##-----------------------
#lines = []
#line = inf.readline()
#while line is not '':
#	while re.match('\s*//',line) or re.match('\s+$',line):
#		# skip comments and white space
#		line = inf.readline()
#	lines.append(line)
#	line = inf.readline()
#inf.close()

inf=open('test.glm','r')
line = inf.readline()

while line is not '':
    m1 = re.match('\s*(\S+) ([^;\s]+)[;\s]',line)
    
    data=open('aa.csv','a')
    
    if m1:
        data.write(line)
        print(m1.group(0))
    line = inf.readline()
inf.close()


#https://blog.csdn.net/pleasecallmewhy/article/details/8929576
#https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000