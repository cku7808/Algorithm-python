import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

result = []
for i, elem in enumerate(b):
    if a[i] == 0:
        result.append(elem)
result.reverse()

for elem in c[:m-len(result)]:
    result.append(elem)
print(*result[:m])
