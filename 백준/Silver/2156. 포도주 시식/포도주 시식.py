import sys
n = int(sys.stdin.readline())

arr = [0]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

result = [0]
result.append(arr[1])
if n>1:
    result.append(arr[1]+arr[2])

    for i in range(3, n+1):
        result.append(max(result[i-2]+arr[i], arr[i-1]+result[i-3]+arr[i], result[i-1]))


print(result[n])
