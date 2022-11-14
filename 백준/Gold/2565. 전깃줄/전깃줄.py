import sys
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

arr.sort()

result = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            result[i] = max(result[i],result[j]+1)
print(n-max(result))
