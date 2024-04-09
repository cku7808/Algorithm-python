import sys

students = set(range(1,31))
assign = set([int(sys.stdin.readline()) for _ in range(28)])

answer = sorted(list(students - assign))
for i in range(2):
    print(answer[i])
