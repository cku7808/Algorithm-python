import sys

n, k = map(int, sys.stdin.readline().split())
nums = []
for i in range(1,n+1):
    if n%i == 0:
        nums.append(i)

nums.sort()
print(nums[k-1] if len(nums) >= k else 0)
