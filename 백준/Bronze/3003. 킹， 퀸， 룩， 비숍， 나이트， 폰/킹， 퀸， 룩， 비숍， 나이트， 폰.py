import sys

arr = list(map(int, sys.stdin.readline().split()))
origin = [1,1,2,2,2,8]

print(*list(map(lambda x,y : x-y, origin, arr)))