"""
Problem: String Validators (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to check for various string properties such as alphanumeric, alphabetic, digits, lowercase, and uppercase.
Link: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Approach: Use the built-in string methods to check for each property.

"""

if __name__ == '__main__':

    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))