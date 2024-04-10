import sys, math

t = int(sys.stdin.readline())
primes = [True]*1000001

for i in range(2, int(math.sqrt(1000000))+1):
    if primes[i]:
        for j in range(i+i,1000001,i):
            primes[j] = False
            
for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    for i in range(2, n//2+1):
        if primes[i] and primes[n-i]:
            cnt += 1
    print(cnt)
