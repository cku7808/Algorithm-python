import sys, heapq

def find(x):
    # if parent[x] != x:
    #     parent[x] = find(parent[x])
    # return parent[x]
    while x != parent[x]: # 3 4
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
parent = [i for i in range(v+1)]
heap = []
ans = 0
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (c, a, b))

while heap:
    cost, u, v = heapq.heappop(heap)
    if find(u) != find(v):
        # print(cost, u, v)
        union(u, v)
        ans += cost
print(ans)