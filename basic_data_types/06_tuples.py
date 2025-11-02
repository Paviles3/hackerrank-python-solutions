""" 

Problem: Tuples (Hackerrank)
Subdomain: Basic Data Types
Difficulty: Easy
Summary: A simple program that creates a tuple from user input and computes its hash value.
Link: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
Approach: Use a tuple to store elements and compute its hash value.

"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    
    print((hash(t)))