import sys
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x:(x[1],x[0]))

result = [arr[0]]
for i in range(1,n):
    start = arr[i][0]
    last = result[-1][1]
    if start >= last:
        result.append(arr[i])
print(len(result))
