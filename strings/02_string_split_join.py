"""
Problem: String Split and Join (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to split a string by spaces and then join it with a hyphen.
Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
Approach: Use the split() method to split the string by spaces and then use the join() method to join the words with a hyphen.

"""

def split_and_join(line):

    line = line.split(" ")
    line = "-".join(line)

    return line

if __name__ == '__main__':

    line = input()
    result = split_and_join(line)
    print(result)