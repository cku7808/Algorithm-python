import sys

def check(col):
    for i in range(col):
        if (track[i] == track[col]) or (abs(track[i]-track[col]) == abs(i-col)):
            return False
    return True

def backtrack(col):
    global ans
    if col == n:
        ans += 1
        return

    for i in range(n):
        track[col] = i
        if check(col):
            backtrack(col+1)

n = int(sys.stdin.readline())
ans = 0
track = [0]*n
backtrack(0)
print(ans)