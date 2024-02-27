from collections import deque
def solution(priorities, location):
    q_prior = deque(priorities)
    q_idx = deque(range(len(priorities)))
    q_cnt = deque([1]*len(priorities))
    
    while q_prior:
        p, i, c = q_prior.popleft(), q_idx.popleft(), q_cnt.popleft()
        if len(q_prior) > 0:
            if p < max(q_prior):
                q_prior.append(p)
                q_idx.append(i)
                q_cnt.append(c)
            else:
                if i == location:
                    return c
                q_cnt = deque([x + 1 for x in q_cnt])
        else:
            if i == location:
                return c
                
            
            
