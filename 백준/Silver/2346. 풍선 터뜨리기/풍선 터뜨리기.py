import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()
nums = list(map(int, sys.stdin.readline().split()))

for idx, elem in enumerate(nums):
    q.append((idx+1,elem))

result = []
while q:
    num, cnt = q.popleft()
    result.append(num)
    if q:
        if cnt < 0:
            for _ in range(abs(cnt)):
                q.appendleft(q.pop())
        else:
            for _ in range(abs(cnt)-1):
                q.append(q.popleft())
        
print(*result)
