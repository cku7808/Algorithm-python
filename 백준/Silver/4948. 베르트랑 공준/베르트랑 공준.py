import sys
def primeCheck(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

prime = []
for i in range(2,246913):
    if primeCheck(i):
        prime.append(i)


while True:
    cnt = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in prime:
        if i>n and i<2*n+1:
            cnt += 1
    print(cnt)
