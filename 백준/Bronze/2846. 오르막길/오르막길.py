import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

max_size = 0
num = 0
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        num += arr[i+1] - arr[i]
    else:
        max_size = num if num > max_size else max_size
        num = 0
if num:
    max_size = num if num > max_size else max_size
print(max_size)