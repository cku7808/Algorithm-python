import sys
from collections import deque
input = sys.stdin.readline

def dfs(start, visited, arr):
    if not visited[start]:
        visited[start] = True
        for elem in graph[start]:
            if elem in arr and not visited[elem]:
                dfs(elem, visited, arr)

def check(red, blue):
    if len(red) == 0 or len(red) == n:
        return sys.maxsize
    red_visited = [False]*(n+1)
    blue_visited = [False]*(n+1)
    dfs(red[0], red_visited, red)
    dfs(blue[0], blue_visited, blue)
    if sum(red_visited) == len(red) and sum(blue_visited) == len(blue):
        return abs(sum(map(lambda x:populations[x], red)) - sum(map(lambda x:populations[x], blue)))
    else:
        return sys.maxsize

def backtrack(cnt, idx):
    global ans
    blue = [elem for elem in range(1, n+1) if elem not in red]
    ans = min(check(red, blue), ans)

    for i in range(idx, n+1):
        red.append(i)
        backtrack(cnt+1, i+1)
        red.pop()

n = int(input())
ans = sys.maxsize
populations = [0]+list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    num, *people = list(map(int, input().split()))
    graph[i].extend(people)

red, blue = [], []
visited = [False]*(n+1)
backtrack(0, 1)
print(-1 if ans == sys.maxsize else ans)