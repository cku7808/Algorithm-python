import sys

n, k = map(int, sys.stdin.readline().split())

lst = {}
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    nation = tmp[0]
    score_list = tmp[1:]

    lst[nation]=score_list

lst = dict(sorted(lst.items(),key=lambda x:(x[1][0],x[1][1],x[1][2]), reverse=True))

rank = 1
for n,l in lst.items():
    if n != k and l != lst[k]:
        rank += 1
    else:
        break
print(rank)
