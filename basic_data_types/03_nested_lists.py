""" 

Problem: Nested Lists (Hackerrank)
Subdomain: Basic Data Types
Difficulty: Easy
Summary: A simple program to create a nested list of student names and their scores, and find the second lowest score along with the names of students who achieved it.
Link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
Approach: Use nested lists to store student names and scores, then find the second lowest score
and the corresponding student names.

"""

if __name__ == '__main__':

    students  = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest = sorted(set([score for name, score in students]))[1]
    
    for name in sorted([n for n, s in students if s == second_lowest]):
        print(name)