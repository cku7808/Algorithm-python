import sys

def solution(stack, idx):
    if len(stack) == 6:
        print(*stack)
        return
    for i in range(idx, k):
        stack.append(nums[i])
        solution(stack, i+1)
        stack.pop()

while True:
    k, *nums = list(map(int, sys.stdin.readline().split()))
    if k == 0:
        break
    
    solution([],0)
    print()