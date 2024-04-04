from collections import deque

def solution(people, limit):
    people = sorted(people)
    left, right = 0, len(people)-1
    answer = 0
    
    while left < right:
        if people[left]+people[right] <= limit:
            left += 1
            answer += 1
        right -= 1
    return len(people) - answer
    
            
        

        