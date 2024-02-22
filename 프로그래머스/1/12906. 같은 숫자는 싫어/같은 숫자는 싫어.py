from collections import deque

def solution(arr):
    original = deque(arr)
    result = deque()

    while original:
        cur = original.popleft()
        if len(original)>0:
            nex = original[0]
            if cur != nex:
                result.append(cur)
        else:
            result.append(cur)
    return list(result)
