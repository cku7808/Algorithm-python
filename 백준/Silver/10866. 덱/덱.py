import sys
from collections import deque

q = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if " " in cmd:
        cmd, x = cmd.split()
        x = int(x)
    
    if cmd == "push_back":
        q.append(x)
    elif cmd == "push_front":
        q.appendleft(x)
    elif cmd == "pop_front":
        print(q.popleft()) if len(q) != 0 else print(-1)
    elif cmd == "pop_back":
        print(q.pop()) if len(q) != 0 else print(-1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(1) if len(q) == 0 else print(0)
    elif cmd == "front":
        print(q[0]) if len(q) != 0 else print(-1)
    else:
        print(q[-1]) if len(q) != 0 else print(-1)
