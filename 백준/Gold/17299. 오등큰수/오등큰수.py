import sys, heapq
from collections import deque

n = int(sys.stdin.readline())
q = deque(map(int, sys.stdin.readline().split()))

cnt_dict = dict()

for elem in q:
    if not cnt_dict.get(elem):
        cnt_dict[elem] = 1
    else:
        cnt_dict[elem] += 1

ngf = [0]*len(q)


# 최소 힙을 이용하기
# 맨 뒤 원소부터 pop해서 힙에 넣기 전에 top 값이 자기보다 크면 ngf 갱신
# 자신보다 값이 작거나 같으면 top을 pop하기
# 이후 heap에 값 넣기

heap = []
while q:
    x = q.pop()
    if len(heap) == 0 :
        ngf[len(q)] = -1
    while len(heap) and heap[0][0] <= cnt_dict[x]:
        heapq.heappop(heap)
    if len(heap) and heap[0][0] > cnt_dict[x]:
        ngf[len(q)] = heap[0][1]
    heapq.heappush(heap, (cnt_dict[x],x))

for i in range(n):
    if ngf[i] == 0:
        ngf[i] = -1
print(*ngf)
