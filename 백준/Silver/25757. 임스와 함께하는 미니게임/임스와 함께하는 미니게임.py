import sys

n, game = sys.stdin.readline().split()
n = int(n)

info = dict()
info["Y"] = 2
info["F"] = 3
info["O"] = 4

names = dict()

cnt = 0
num = 1
for _ in range(n):
    name = sys.stdin.readline().strip()
    try:
        if names[name]:
            pass
    except:
        names[name] = True
        num += 1
        if info[game] == num:
            cnt += 1
            num = 1
print(cnt)
