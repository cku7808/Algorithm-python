import sys

n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

left, right = 1, max(height)

while left <= right:
    mid = (left+right) // 2
    nums = 0
    for elem in height:
        if elem >= mid:
            nums += elem - mid
    if nums >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
