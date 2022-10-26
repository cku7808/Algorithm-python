import sys
n = int(sys.stdin.readline())

cnt = 0
def fib(n):
    global cnt
    if n==1 or n==2:
        cnt += 1
        return 1
    return fib(n-1)+fib(n-2)

fib(n)
res1 = cnt
res2 = n-2
print(res1, res2)
