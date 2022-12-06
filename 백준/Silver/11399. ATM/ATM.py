import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

ans = arr[0]
result = arr[0]
for i in range(1,n):
    ans += arr[i]
    result += ans
print(result)
