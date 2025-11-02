"""
Problem: sWAP cASE (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to swap the case of each character in a string.
Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
Approach: Use the swapcase() method of the string class to swap the case of each character.


"""

def swap_case(s):

    return s.swapcase()


if __name__ == '__main__':

    s = input()
    result = swap_case(s)
    print(result)