""" 

Problem: Lists (Hackerrank)
Subdomain: Basic Data Types
Difficulty: Easy
Summary: A simple program to perform various list operations based on user input.
Link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
Approach: Use a list to store elements and perform operations like insert, remove, append, sort, pop, and reverse.          

"""

if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    for _ in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            list.insert(int(command[1]), int(command[2]))
            
        elif command[0] == 'print':
            print(list)
        
        elif command[0] == 'remove':
            list.remove(int(command[1]))
            
        elif command[0] == 'append':
            list.append(int(command[1]))
            
        elif command[0] == 'sort':
            list.sort()
            
        elif command[0] == 'pop':
            list.pop()
            
        elif command[0] == 'reverse':
            list.reverse()
        