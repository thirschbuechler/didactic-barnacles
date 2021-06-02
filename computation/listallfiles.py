# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:38:54 2020

@author: https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
"""
import os #os module imported here
location = os.getcwd() # get present working directory location here
counter = 0 #keep a count of all files found
csvfiles = [] #list to store all csv files found at location
filebeginwithhello = [] # list to keep all files that begin with 'hello'
otherfiles = [] #list to keep any other file that do not match the criteria

for file in os.listdir(location):
    try:
        if file.endswith(".csv"):
            print( "csv file found:\t", file)
            csvfiles.append(str(file))
            counter = counter+1

        elif file.endswith(".csv"): #because some files may start with hello and also be a csv file
            print( "csv file found:\t", file)
            csvfiles.append(str(file))
            counter = counter+1

        elif file.startswith("hello"):
            print( "hello files found: \t", file)
            filebeginwithhello.append(file)
            counter = counter+1

        else:
            otherfiles.append(file)
            print(file)
            counter = counter+1
    except Exception as e:
        raise e
        print("No files found here!")

print("Total files found:\t", counter)