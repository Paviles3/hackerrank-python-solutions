"""
Problem: Mutations (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to mutate a string by replacing a character at a specific position.
Link: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
Approach: Convert the string to a list, replace the character, and then join the list back into a string.
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string
    
if __name__ == '__main__':

    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)