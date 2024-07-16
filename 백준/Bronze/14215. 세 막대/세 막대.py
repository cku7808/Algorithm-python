import sys
from itertools import combinations

a, b, c = map(int, sys.stdin.readline().split())

nums = sorted([a,b,c])

if nums[-1] >= sum(nums[:-1]):

    nums[-1] -= nums[-1]-sum(nums[:-1])+1

print(sum(nums))
