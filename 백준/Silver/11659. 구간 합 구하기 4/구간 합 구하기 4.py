import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix = arr[:]
for i in range(1,n):
    prefix[i] += prefix[i-1]

arr.insert(0,0)
prefix.insert(0,0)

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    print(prefix[j] - prefix[i-1])
