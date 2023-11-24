from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    if (sum_q1 + sum_q2)%2 != 0:
        return -1
    
    for cnt in range(300000):
        if sum_q1 == sum_q2:
            return cnt
        elif sum_q1 > sum_q2:
            num = queue1.popleft()
            queue2.append(num)
            sum_q2 += num
            sum_q1 -= num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum_q1 += num
            sum_q2 -= num

    return -1
