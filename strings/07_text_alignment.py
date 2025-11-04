"""
Problem: Text Alignment (Hackerrank)
Subdomain: Strings
Difficulty: Easy
Summary: A simple program to demonstrate text alignment using string methods such as center(), ljust(), and rjust().
Link: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Approach: Use the built-in string methods to check for each property.

"""

if __name__ == '__main__':

    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))            

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))    

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))