import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

left, right = 1, m
if sum(arr) <= m:
    print(max(arr))
else:
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for num in arr:
            total += num if num < mid else mid

        if total > m:
            right = mid - 1
        else:
            left = mid + 1

    print(right)
