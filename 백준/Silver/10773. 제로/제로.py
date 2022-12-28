import sys
from collections import deque
k = int(sys.stdin.readline())
q = deque()

for _ in range(k):
    inp = int(sys.stdin.readline())
    if inp == 0:
        q.pop()
    else:
        q.append(inp)
print(sum(q))
