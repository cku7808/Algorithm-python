import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    arr.append((a,b))

arr.sort(key = lambda x: (x[0],x[1]))

for elem in arr:
    a,b = elem[0], elem[1]
    print(a,b)
