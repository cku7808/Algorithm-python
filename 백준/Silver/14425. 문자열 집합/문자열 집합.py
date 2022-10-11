import sys
n,m = map(int, sys.stdin.readline().split())
ns = []
for _ in range(n):
    ns.append(sys.stdin.readline().strip())
ms = []
cnt = 0
for _ in range(m):
    s = sys.stdin.readline().strip()
    if s in ns:
        cnt += 1
print(cnt)



    
