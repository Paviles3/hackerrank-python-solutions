"""
Problem: Designer Door Mat (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to create a designer door mat pattern using string manipulation and formatting.   
Link: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
Approach: Use string multiplication and the center() method to create the desired pattern.

"""

if __name__ == '__main__':

    n, m = map(int, input().split())

    # Top half
    for i in range(1, n, 2):
        pattern = ('.|.' * i).center(m, '-')
        print(pattern)

    # Middle line
    print('WELCOME'.center(m, '-'))

    # Bottom half
    for i in range(n - 2, 0, -2):
        pattern = ('.|.' * i).center(m, '-')
        print(pattern)