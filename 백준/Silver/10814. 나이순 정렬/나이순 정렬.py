import sys

n = int(sys.stdin.readline())
user = []
for _ in range(n):
    year,name = sys.stdin.readline().strip().split()
    user.append((int(year),name))

user.sort(key=lambda x:x[0])

for elem in user:
    print(elem[0],elem[1])

