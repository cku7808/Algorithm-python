import sys, heapq, math
from itertools import combinations
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
pos = [0]*(n+1)
candidates = set()

parent = list(range(n+1))

for i in range(n):
    x, y = map(int, input().split())
    pos[i+1] = (x, y)
    candidates.add(i+1)

for _ in range(m):
    p1, p2 = map(int, input().split())
    union(p1, p2)

heap = []
for comb in combinations(range(1, n+1), 2):
    p1, p2 = comb[0], comb[1]
    x1, y1 = pos[p1][0], pos[p1][1]
    x2, y2 = pos[p2][0], pos[p2][1]
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    heapq.heappush(heap, (dist, comb[0], comb[1]))

ans = 0
while heap:
    dist, p1, p2 = heapq.heappop(heap)
    if find(p1) != find(p2):
        union(p1, p2)
        ans += dist
print("{:.2f}".format(ans))