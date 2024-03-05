from collections import deque
import sys

def solution(n, wires):
    answer = sys.maxsize
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        edge_nums = []
        for j, edges in enumerate(wires):
            if i != j:
                u, v = edges
                edge_nums.append(u)
                graph[u].append(v)
                graph[v].append(u)

        q = deque()
        q.append(edge_nums[0])

        visited = [False]*(n+1)
        cnt = 1

        while q:
            cur = q.popleft()
            visited[cur] = True
            for elem in graph[cur]:
                if not visited[elem]:
                    q.append(elem)
                    cnt += 1

        answer = min(answer, abs(cnt-(n-cnt)))
    return answer
        
            
        
    
    
        
        