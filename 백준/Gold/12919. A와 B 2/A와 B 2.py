import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

def transform(t):
    if t == s:
        print(1)
        sys.exit()
        
    if len(t) == 0:
        return

    if t[-1] == "A":
        transform(t[:-1])
    if t[0] == "B":
        transform(t[1:][::-1])
        
transform(t)
print(0)
