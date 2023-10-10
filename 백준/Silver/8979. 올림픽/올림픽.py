import sys

n, k = map(int, sys.stdin.readline().split())

lst = {}
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    nation = tmp[0]
    score_list = tmp[1:]
    score_list[0] *= 3
    score_list[1] *= 2
    score = sum(score_list)

    lst[nation]=score

lst = dict(sorted(lst.items(),key=lambda x:x[1], reverse=True))
rank = 1
for elem in lst.values():
    if elem > lst[k]:
        rank += 1
print(rank)
        
