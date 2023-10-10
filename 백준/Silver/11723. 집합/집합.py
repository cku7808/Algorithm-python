import sys

m = int(sys.stdin.readline())

s = set()

for _ in range(m):
    tmp = sys.stdin.readline().split()
    cmd = tmp[0]

    if cmd == "all" :
        s = set(range(1,21))
    elif cmd == "empty" :
        s = set()
    elif cmd == "add" :
        s.add(int(tmp[1]))
    elif cmd == "remove" :
        s.discard(int(tmp[1]))
    elif cmd == "check":
        print(1 if int(tmp[1]) in s else 0)
    else:
        s.discard(int(tmp[1])) if int(tmp[1]) in s else s.add(int(tmp[1]))
