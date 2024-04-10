import sys, math

t = int(sys.stdin.readline())

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
    return True

for _ in range(t):
    n = int(sys.stdin.readline())

    while not isPrime(n):
        n += 1
    print(n)
    
    
