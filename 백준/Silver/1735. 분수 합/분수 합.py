import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

tail = b*d
head = b*c + a*d

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

num = gcd(tail, head)

print(head//num, tail//num)

