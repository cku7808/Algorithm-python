import sys
input = sys.stdin.readline

t = int(input())

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(t):
    n, m = map(int, input().split())
    parent = list(range(n+1))
    ans = 0
    for i in range(m):
        a, b = map(int, input().split())
        if find(a) != find(b):
            ans += 1
            union(a, b)
    print(ans)