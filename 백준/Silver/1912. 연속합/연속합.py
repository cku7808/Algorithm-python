import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = []
result.append(arr[0])
for i in range(1,n):
    if arr[i] > arr[i]+result[i-1]:
        result.append(arr[i])
    else:
        result.append(arr[i]+result[i-1])
        


print(max(result))
