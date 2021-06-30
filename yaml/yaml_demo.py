#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:27:20 2021

@author: thomas 
sources: stackabuse
"""
import yaml as yl #pyyaml >5.4 to be sav(er) from arbitrary code exec
import numpy as np

def fruity():
    with open('fruits.yaml',"w") as file:
        fruits={ 'apples': 20, 'mangoes': 2, 'bananas': 3, 'grapes': 100, 'pineapples': 1 }
        yl.dump(fruits,file)#also sorts, apparently
    
    
    with open('fruits.yaml',"r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits = yl.safe_load(file)
        print(fruits)
        
        
def foody():
    with open('foods.yaml',"w") as file:
        fruits={ 'apples': 20, 'mangoes': 2, 'bananas': 3, 'grapes': 100, 'pineapples': 1 }
        meats={"chicken":3, "beef":1, "fish":99, "pork":3}
        #foods=[fruits, meats]#works but ugly
        foods={"fruits":fruits, "meats":meats}
        yl.dump(foods,file)#also sorts, apparently
    
    
    with open('foods.yaml',"r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        stuff = yl.safe_load(file)
        print(stuff)
     

class msrvalues(object):
    def __init__(self, **entries): 
        # empty defaults
        self.msr_values=[]
        self.msr_title=""
        
        # case readback
        self.__dict__.update(entries)

        
    # do that via public properties, e.g. ".msr_values" etc.
    # def set_and_get_everyting(): bla
    
    def __str(self):
        return self.mystr()
    
    #def __repr__(self): # does not like being defined
    #    return self.mystr()
        
    def mystr(self):
        return("I am {} and my min/max is {}/{}".format( self.msr_title,np.min(np.array(self.msr_values)),np.max(np.array(self.msr_values)) ) )
    
        
def classy(stuff):
    with open('msr.yaml',"w") as file:
        yl.dump(stuff,file)#also sorts, apparently
    
    print("saved, now read..")
    
    with open('msr.yaml',"r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        res = yl.load(file, Loader=yl.BaseLoader)
    
    print("loaded")
    return res

def classystest():
    
    msr_values_orig = msrvalues()
    msr_values_orig.msr_title="a very refined msr"
    msr_values_orig.msr_values=[1,2,3,4]
    print(msr_values_orig.mystr())
    
    
    readback = classy(msr_values_orig)
    
    #now, a dict
    print(str(readback))
    
    #now, class instance
    phoenix = msrvalues(**readback)
    print((phoenix))
    print(phoenix.msr_values)
    
def matrixy():
    stuff=np.matrix([ [1,2],[3,4] ])
    with open('mx.yaml',"w") as file:
        yl.dump(stuff,file)#also sorts, apparently
    
    print("saved, now read..")
    
    with open('mx.yaml',"r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        res = yl.load(file, Loader=yl.BaseLoader)
    
    print("loaded")
    print(res)
    print(np.matrix(res))
 

if __name__ == '__main__': # test if called as executable, not as library, regular prints allowed
         #fruity()
         #foody()
         #classytest()
         matrixy()