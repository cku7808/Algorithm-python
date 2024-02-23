import sys
sys.setrecursionlimit(10 ** 9)

def solution(numbers, target):
    global cnt
    cnt = 0
    def dfs(i, num): # 현재 원소, 합, 방법의 수
        global cnt
        if i == len(numbers):
            if num == target:
                cnt += 1
            return

        dfs(i+1, num+numbers[i])
        dfs(i+1, num-numbers[i])
        return
        
    dfs(0, 0)
    return cnt