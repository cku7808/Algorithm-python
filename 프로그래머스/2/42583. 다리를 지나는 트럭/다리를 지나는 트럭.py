from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    wait = deque(truck_weights)
    ing = deque([0]*bridge_length)
    ing_weight = 0
    while True:
        cnt += 1
        if len(wait) > 0 and ing_weight+wait[0] <= weight and sum(list(map(bool,ing))) <= bridge_length:
            cur = wait.popleft()
            ing[-1] = cur
            ing_weight += cur
        if ing[0]:
            ing_weight -= ing[0]
            ing[0] = 0
            
        ing.append(ing.popleft())
        if len(wait) == 0 and ing_weight == 0:
            return cnt+1


        
            
    