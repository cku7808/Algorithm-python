import sys
n, m = map(int, sys.stdin.readline().split())
pd = {}
for i in range(n):
    pd[i+1] = sys.stdin.readline().strip()

reverse_pd = dict(map(reversed,pd.items()))
for _ in range(m):
    qst = sys.stdin.readline().strip()
    try:
        qst = int(qst)
    except:
        print(reverse_pd[qst])
    else:
        print(pd[qst])

