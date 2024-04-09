import sys

s = sys.stdin.readline().strip()
if len(s)%2 == 0 and s[:len(s)//2] == s[len(s)//2:][::-1]:
    print(1)
elif s[:len(s)//2] == s[len(s)//2+1:][::-1]:
    print(1)
else:
    print(0)