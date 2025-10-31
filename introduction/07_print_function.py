""""
Problem: Print Function (Hackerrank)
Subdomain: Introduction
Difficulty: Easy
Summary: A program to print the numbers from 1 to n without spaces.
Link: https://www.hackerrank.com/challenges/python-print-function/problem?isFullScreen=true
Approach: Use a loop to iterate through the numbers and print them as a string without spaces.

"""
if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        print(i, end='')