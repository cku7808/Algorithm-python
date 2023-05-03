def solution(array):
    a = list(set(array)) # 1 2 3 4
    b = []
    for elem in a:
        b.append(array.count(elem))
    Max = max(b)
    max_idx = b.index(Max)
    
    if b.count(Max) > 1:
        return -1
    else:
        return a[max_idx]