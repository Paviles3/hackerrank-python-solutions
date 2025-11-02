""" 

Problem: Find the Runner-Up Score (Hackerrank)
Subdomain: Basic Data Types
Difficulty: Easy
Summary: A simple program to find the runner-up score from a list of integers.
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Approach: Use set to remove duplicates and then sort to find the second highest score.

"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    sorted_scores = sorted(set(arr))

    runner_up = sorted_scores[-2]
    print(runner_up)