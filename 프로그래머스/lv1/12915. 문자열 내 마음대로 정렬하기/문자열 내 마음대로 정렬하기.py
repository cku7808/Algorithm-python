def solution(strings, n):
    arr = []
    answer = []
    for elem in strings:
        arr.append((elem[n],elem))
    arr.sort()
    for tmp, elem in arr:
        answer.append(elem)
    return answer