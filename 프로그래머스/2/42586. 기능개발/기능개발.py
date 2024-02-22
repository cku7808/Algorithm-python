import math
def solution(progresses, speeds):
    answer = []
    days_left = []
    for i in range(len(progresses)):
        days_left.append(math.ceil((100-progresses[i])/speeds[i]))
        
    date = days_left[0]
    cnt = 1
    for elem in days_left[1:]:
        if elem <= date:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            date = elem
    answer.append(cnt)
    return answer