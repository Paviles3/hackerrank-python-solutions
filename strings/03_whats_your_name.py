"""
Problem: What's Your Name? (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to concatenate a first name and last name with a greeting.
Link: https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
Approach: Use the format() method to concatenate the names with a greeting.

"""

def print_full_name(first_name, last_name):

    print("Hello {} {}! You just delved into python.".format(first_name, last_name))

if __name__ == '__main__':

    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)