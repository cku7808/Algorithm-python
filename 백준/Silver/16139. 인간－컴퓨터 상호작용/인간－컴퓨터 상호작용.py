import sys
S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

arr = [[0]*26 for i in range(len(S))]

for i in range(len(S)):
    for j in range(26):
        if ord(S[i])-97 == j:
            arr[i][j] = arr[i-1][j]+1
        else:
            arr[i][j] = arr[i-1][j]

for _ in range(q):
    s,l,r = sys.stdin.readline().split()
    l, r = int(l), int(r)
    if l == 0:
        print(arr[r][ord(s)-97])
    else:
        print(arr[r][ord(s)-97]-arr[l-1][ord(s)-97])
