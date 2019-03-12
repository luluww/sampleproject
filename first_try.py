# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:21:57 2019

@author: wanda
"""
import re

def find_num_word_in_file(filename,word):
    f=open(filename,'r')
    text=f.read()
    words=text.split()
    num=0
    for w in words:
        if w==word:
            num+=1
    return num

f=open('trump1.txt')
text=f.readline()

for line in text:
    line=line.rstrip()
    if re.search('[0-9]+',line):
        print('$')


