"""
Problem: Find a String (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to count the number of occurrences of a substring in a string.
Link: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
Approach: Use the count() method of the string class to count the occurrences of the substring.

"""

def count_substring(string, sub_string):

    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1

    return count

if __name__ == '__main__':

    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)