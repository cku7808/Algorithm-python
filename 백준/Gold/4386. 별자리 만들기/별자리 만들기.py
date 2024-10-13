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

n = int(input())
heap = []
stars = []
parent = list(range(n))
ans = 0
for _ in range(n):
    stars.append(tuple(map(float, input().split())))

for elem in combinations(range(n), 2):
    star1, star2 = stars[elem[0]], stars[elem[1]]
    dist = math.sqrt((star1[0]-star2[0])**2 + (star1[1]-star2[1])**2)
    heapq.heappush(heap, (dist, elem[0], elem[1]))

while heap:
    cost, star1_idx, star2_idx = heapq.heappop(heap)
    if find(star1_idx) != find(star2_idx):
        union(star1_idx, star2_idx)
        ans += cost
print(ans)