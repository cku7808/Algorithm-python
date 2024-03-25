import heapq

def solution(jobs):
    heap = []
    start, now, cnt = -1, 0, 0
    result = 0
    
    while cnt < len(jobs):
        for elem in jobs:
            if start < elem[0] <= now:
                heapq.heappush(heap, (elem[1], elem[0]))
        if heap:
            # while heap:
            take_time, start_time = heapq.heappop(heap)
            start = now
            now += take_time
            result += now - start_time
            cnt += 1
        else:
            now += 1
    return result//len(jobs)
            


    