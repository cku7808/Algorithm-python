from itertools import permutations
import math

def solution(numbers):
    max_nums = len(numbers)
    possible = set(list(map(int, numbers)))
    
    for i in range(2,len(numbers)+1):
        for elem in permutations(numbers, i):
            possible.add(int("".join(elem)))

    cnt = 0
    for elem in list(possible):
        if elem not in [0,1]:
            flag = True
            for i in range(2,int(math.sqrt(elem))+1):
                if int(elem) % i == 0:
                    flag = False
                    break
            if flag: cnt += 1
    return cnt
        
    
