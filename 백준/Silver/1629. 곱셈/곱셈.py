import sys

a, b, c = map(int, sys.stdin.readline().split())

def modular(a,b,c):
    if b == 1:
        return a%c
    ans = modular(a,b//2,c)
    if b % 2 == 0:
        return (ans*ans)%c
    else:
        return (ans*ans*a)%c
print(modular(a,b,c))
