import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    n = len(scoville)
    for _ in range(n):
        if len(scoville) >= 1:
            first = scoville[0]
            if first >= K:
                return answer
            first = heapq.heappop(scoville)
        if len(scoville) >= 1:
            second = heapq.heappop(scoville)

            new = first + (second*2)
            answer += 1
            heapq.heappush(scoville, new)
            
    return -1
