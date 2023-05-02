def solution(numbers, k):
    cnt = 1
    next = 0 # 인덱스 
    while True:
        if cnt == k:
            break
        # 공 던짐 
        next = (next+2)%(len(numbers)) #2 
        cnt += 1
    return numbers[next]