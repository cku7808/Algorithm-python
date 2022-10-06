import sys, heapq
from heapq import heapify,heappop

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

#card 정렬 - 힙 정렬
sorted_card = []
heapify(card)
for i in range(n):
    tmp = heappop(card)
    sorted_card.append(tmp)

#카드 찾기 - 이진 탐색

for elem in check:
    left = 0
    right = n-1
    ans = 0
    while left<=right:
        mid = (left+right)//2
        if elem == sorted_card[mid]:
            ans = 1
            break
        elif elem > sorted_card[mid]:
            left = mid+1
        else:
            right = mid-1
        
    print(ans, end=" ")

