import sys
from collections import deque
t = int(sys.stdin.readline())

def cal(arr):
    org = deque(arr)
    tmp = deque()
    cnt = 1
    while cnt <= len(arr):
        result = org.pop()
        if result == ")":
            tmp.append(result)
        else:
            if len(tmp) != 0 and tmp[-1] == ")":
                tmp.pop()
            else:
                tmp.append(result)
        cnt += 1
    if len(tmp) == 0:
        return "YES"
    else:
        return "NO"
    


for _ in range(t):
    arr = sys.stdin.readline().strip()
    ans = cal(arr)
    print(ans)
