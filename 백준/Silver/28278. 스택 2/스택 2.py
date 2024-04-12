import sys
from collections import deque

n = int(sys.stdin.readline())

stack = deque()

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith("1"):
        stack.append(command.split()[-1])
    elif command.startswith("2"):
        print(stack.pop() if stack else "-1")
    elif command.startswith("3"):
        print(len(stack))
    elif command.startswith("4"):
        print("1" if not stack else "0")
    else:
        print(stack[-1] if stack else "-1")