import heapq,sys
from heapq import heapify

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

heapify(arr)
for i in range(n):
    print(heapq.heappop(arr))
    
