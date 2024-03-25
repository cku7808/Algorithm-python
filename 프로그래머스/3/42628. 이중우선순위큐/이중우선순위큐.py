import heapq
def solution(operations):
    q = []

    for op in operations:
        if op == "D 1":
            if q: q.pop()
        elif op == "D -1":
            if q: heapq.heappop(q)
        else:
            num = int(op.split(" ")[-1])
            heapq.heappush(q, num)
            q.sort()
    if q:
        return [q[-1], q[0]]
    else:
        return [0, 0]