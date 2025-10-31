""" 

Problem: Write a Function (Hackerrank)
Subdomain: Introduction
Difficulty: Medium
Summary: A program to determine if a given year is a leap year.
Link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
Approach: Use conditional statements to determine if a year is a leap year.

"""

def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))