#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://adventofcode.com/2019/day/1/

import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def calculate_fuel(x):
    fuel = round_down(int(x)/3)-2
    if fuel <= 0:
        fuel=0
    return fuel

result=0

with open('day1-values.txt') as f:
   for line in f:
        fuel = calculate_fuel(int(line))
        # Part 1
        result+=fuel
        # Part 2        
        while True:
            fuel = calculate_fuel(int(fuel))
            result+=fuel
            if fuel == 0:
                break
print(result)
