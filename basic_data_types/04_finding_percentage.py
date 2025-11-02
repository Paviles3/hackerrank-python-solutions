""" 

Problem: Finding the Percentage (Hackerrank)
Subdomain: Basic Data Types
Difficulty: Easy
Summary: A simple program to calculate the average percentage score of a student from a list of student marks.
Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
Approach: Use a dictionary to store student names and their scores, then calculate the average score for a specific student.

"""

if __name__ == '__main__':

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    print(f"{avg:.2f}")
