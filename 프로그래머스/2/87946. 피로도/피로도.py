ans = 0
def dfs(dungeons, k, cnt, visited):
    global ans
    ans = max(cnt, ans)
    for i in range(len(dungeons)):
        need, sub = dungeons[i]
        if not visited[i] and k >= need:
            visited[i] = True
            dfs(dungeons, k-sub, cnt+1, visited)
            visited[i] = False
            
def solution(k, dungeons):
    global ans
    visited = [False]*len(dungeons)
    dfs(dungeons, k, 0, visited)
    return ans   