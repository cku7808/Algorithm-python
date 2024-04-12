import sys
from collections import deque

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
nexts = 1
stack = deque()

for elem in line:
    stack.append(elem)
    while stack and stack[-1] == nexts:
        stack.pop()
        nexts += 1
if stack:
    print("Sad")
else:
    print("Nice")