"""
Problem: Text Wrap (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to wrap a given string into a paragraph of a specified width.
Link: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Approach: Use the built-in string methods to check for each property.

"""

import textwrap

def wrap(string, max_width):
    
    return '\n'.join(textwrap.wrap(string, max_width))

# Manual implementation without textwrap module
    # result = ''
    # for i in range(0, len(string), max_width):
    #     result += string[i:i+max_width] + '\n'
    # return result.rstrip()  

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)