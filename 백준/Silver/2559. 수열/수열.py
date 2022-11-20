import sys
n,k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

max_num = sum(arr[:k])
tmp = sum(arr[:k])

for i in range(k,n):
    tmp = tmp + arr[i] - arr[i-k]
    max_num = max(max_num,tmp)

print(max_num)
