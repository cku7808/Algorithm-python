import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(sys.stdin.readline())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    a = max(x,y)
    b = min(x,y)
    print(a*b // gcd(a,b))

        
