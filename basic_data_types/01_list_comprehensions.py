""" 

Problem: List Comprehensions (Hackerrank)
Subdomain: Basic Data Types
Difficulty: Easy
Summary: A simple program to demonstrate list comprehensions in Python.
Link: https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
Approach: Use list comprehensions to generate a list of coordinates based on given conditions.

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    nestedList = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)]

    print(nestedList)