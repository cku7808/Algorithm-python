import sys

k, n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]

left, right = 1, max(lines)

while left <= right:
    mid = (right+left)//2
    nums = 0
    for elem in lines:
        nums += elem//mid
    if nums >= n:
        left = mid+1
    else:
        right = mid-1
print(right)
