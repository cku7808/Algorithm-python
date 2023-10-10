import sys

n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

def solution(stack, idx):
    if len(stack) == m:
        print(*stack)
        return

    for i in range(n):
        if lst[i] not in stack:
            stack.append(lst[i])
            solution(stack, i+1)
            stack.pop()

solution([], 0)
