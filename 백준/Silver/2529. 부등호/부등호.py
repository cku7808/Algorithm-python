import sys

k = int(sys.stdin.readline())
simbols = list(sys.stdin.readline().split())
nums = list(range(10))

def check(arr, simbols):
    for i in range(k):
        if simbols[i] == "<" and arr[i] > arr[i+1]:
            return False
        elif simbols[i] == ">" and arr[i] < arr[i+1]:
            return False
    return True

min_answer = "".join(map(str,list(range(9,9-k-1,-1))))
max_answer = "".join(map(str,list(range(k+1))))

result = []
visited = [False]*10
def backtrack(visited):
    global min_answer, max_answer
    
    if len(result) == k+1:
        if check(result, simbols):
            tmp = "".join(map(str,result))
            min_answer = min(min_answer, tmp)
            max_answer = max(max_answer, tmp)
            return
        
    for i in range(10):
        if not visited[i]:
            result.append(i)
            visited[i] = True
            backtrack(visited)
            result.pop()
            visited[i] = False
            
backtrack(visited)
print(max_answer.rjust(k+1,"0"))
print(min_answer.rjust(k+1,"0"))
