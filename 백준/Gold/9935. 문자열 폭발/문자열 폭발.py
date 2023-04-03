import sys
from collections import deque

s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
for elem in s:
    stack.append(elem)
    if "".join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
