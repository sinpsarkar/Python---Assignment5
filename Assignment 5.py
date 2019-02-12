# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:32:06 2019

@author: psarka
"""

#1. Write a function to compute 5/0 and use try/except to catch the exceptions.

import sys

def DivideByZero(x):
    try:
        x/0
    except ZeroDivisionError as e:
        print("Error: ",str(e).upper())


x=5
DivideByZero(x)


#2. Implement a Python program to generate all sentences where subject is in ["Americans",
#"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Sentence = [(Sub+' '+vrb+' '+Obj+".") for Sub in subjects for vrb in verbs for Obj in objects]
print("Output:")
for sen in Sentence:    
    print(sen)
    

