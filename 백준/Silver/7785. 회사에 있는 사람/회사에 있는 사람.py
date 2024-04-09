import sys

n = int(sys.stdin.readline())
log = dict()

for _ in range(n):
    name, state = sys.stdin.readline().strip().split()
    if state == "enter":
        log[name] = True
    else:
        del log[name]

for elem in sorted(log.keys(),reverse=True):
    print(elem)