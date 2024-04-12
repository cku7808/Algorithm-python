import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith("push"):
        q.append(int(command.split()[-1]))
    elif command.startswith("pop"):
        print(q.popleft() if q else -1)
    elif command.startswith("size"):
        print(len(q))
    elif command.startswith("empty"):
        print(1 if not q else 0)
    elif command.startswith("front"):
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
