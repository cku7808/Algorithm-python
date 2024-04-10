import sys

n = int(sys.stdin.readline())
origin = [int(sys.stdin.readline()) for _ in range(n)]

diff = []
for i in range(n-1):
    diff.append(origin[i+1] - origin[i])

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

num = diff[0]
for i in range(1,n-1):
    a, b = max(num, diff[i]), min(num, diff[i])
    num = gcd(a,b)

print((origin[-1]-origin[0])//num +1 - n)
    
