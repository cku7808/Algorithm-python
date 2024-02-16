import sys

n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (end + start)//2
    cur = house[0]
    cnt = 1

    for i in range(1,n):
        if house[i] >= mid+cur:
            cnt += 1
            cur = house[i]

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)