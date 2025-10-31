""" 

Problem: Loops (Hackerrank)
Subdomain: Introduction
Difficulty: Easy
Summary: A program to the print the squares of all non-negative integers less than a given integer.
Link: https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
Approach: Use a loop to iterate through the numbers and print their squares.

"""
if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)