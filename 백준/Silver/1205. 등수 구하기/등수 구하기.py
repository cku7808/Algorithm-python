import sys

n, score, p = map(int, sys.stdin.readline().split())
if n != 0:
    arr = list(map(int, sys.stdin.readline().split()))
else:
    arr = []

pos = 0 
for i in range(len(arr)):
    if arr[i] >= score:
        pos = i+1

if p <= pos:
    print(-1)
else:
    arr.append(score)
    arr.sort(reverse=True)
    arr = arr[:p]
    print(arr.index(score)+1)
