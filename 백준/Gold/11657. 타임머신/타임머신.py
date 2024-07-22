import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

inf = float("inf")
edges = []

dist = [inf]*(n+1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

def bf(start):
    dist[start] = 0

    for i in range(n):
        for edge in edges:
            cur, nxt, cost = edge
            if dist[cur] != inf and dist[cur] + cost < dist[nxt]:
                dist[nxt] = dist[cur] + cost
                if i == n-1:
                    return False
    return True

if bf(1):
    for elem in dist[2:]:
        if elem == inf:
            print(-1)
        else:
            print(elem)
else:
    print(-1)