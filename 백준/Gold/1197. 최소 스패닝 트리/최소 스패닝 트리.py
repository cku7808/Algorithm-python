import sys, heapq
input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())
parent = list(range(v+1))
heap = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

total_weight = 0
while heap:
    cost, x, y = heapq.heappop(heap)
    if find(x) != find(y):
        union(x, y)
        total_weight += cost
print(total_weight)