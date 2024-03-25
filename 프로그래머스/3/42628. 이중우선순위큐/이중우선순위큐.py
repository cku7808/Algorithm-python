import heapq
def solution(operations):
    arr = []
    for command in operations:
        if command[0] == "I":
            heapq.heappush(arr, int(command[2:]))
            # print("push %d result : "%(int(command[2:])),arr)
        else:
            if arr:
                if command[2:] == "1":
                    arr = list(map(lambda x:-x, arr))
                    heapq.heapify(arr)
                    num = heapq.heappop(arr)
                    arr = list(map(lambda x:-x, arr))
                    heapq.heapify(arr)
                    # print("pop max %d result : "%(-num),arr)
                else:
                    num = heapq.heappop(arr)
                    # print("pop min %d result : "%(num),arr)
    if arr:
        return [max(arr), min(arr)]
    else:
        return [0,0]

                
            