import sys
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_node(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union_node(parent, a, b)
    else:
        print("yes" if find_parent(parent, a) == find_parent(parent, b) else "no")
