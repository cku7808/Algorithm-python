import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

prefix_sum = []
answer = 0
num = 0
etcs = [0]*m
for elem in a:
    num += elem
    prefix_sum.append(num)
    if num%m == 0:
        answer += 1
    etcs[num%m] += 1

for elem in etcs:
    answer += elem*(elem-1)//2
print(answer)
