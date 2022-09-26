import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())

def facto(n):
    if n == 0:
        return 1
    else:
        return n*facto(n-1)

print(facto(n))
