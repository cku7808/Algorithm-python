import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    com = sys.stdin.readline().strip()

    if com.startswith("1"):
        q.appendleft(int(com.split()[-1]))
    elif com.startswith("2"):
        q.append(int(com.split()[-1]))
    elif com.startswith("3"):
        print(q.popleft() if q else -1)
    elif com.startswith("4"):
        print(q.pop() if q else -1)
    elif com.startswith("5"):
        print(len(q))
    elif com.startswith("6"):
        print(1 if not q else 0)
    elif com.startswith("7"):
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
