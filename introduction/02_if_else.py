""" 

Problem: Python If-Else (Hackerrank)
Subdomain: Introduction
Difficulty: Easy
Summary: A program to determine if a given integer is "Weird" or "Not Weird" based on specific conditions.
Link: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
Approach: Use conditional statements to determine if a number is "Weird" or "Not Weird" based on the given criteria.

"""

import math
import os
import random
import re   
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")