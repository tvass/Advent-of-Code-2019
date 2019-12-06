#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://adventofcode.com/2019/day/2/

def multipleFour(n):
    return not(n & 3)

def adds(index):
    values[values[index+3]]=values[values[index+1]]+values[values[index+2]]
    
def multiplies(index):
    values[values[index+3]]=values[values[index+1]]*values[values[index+2]]

def run(noun, verb, values):
    values[1]=noun
    values[2]=verb
    index = 0
    for i in values:
        if(multipleFour(index)):
            if(i == 99):
                break
            elif(i ==1):
                adds(index)
            elif(i ==2):
                multiplies(index)
        index +=1
    return(values)

for i in range(0,99):
    for j in range(0,99):
        values = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
        values = run(i,j,values)
        if values[0]==19690720:
            print(i*100+j)
