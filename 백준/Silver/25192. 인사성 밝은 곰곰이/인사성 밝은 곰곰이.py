import sys

n = int(sys.stdin.readline())

name_dict = dict()
cnt = 0
for _ in range(n):
    command = sys.stdin.readline().strip()
    if command != "ENTER":
        try:
            name_dict[command]
        except:
            name_dict[command] = True
            cnt += 1
    else:
        name_dict = dict()
print(cnt)