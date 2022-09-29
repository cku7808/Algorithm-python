import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
result = []
def hanoi(n,source,dest,temp):
    if n==1:
        result.append((source,dest))
        return
    
    hanoi(n-1,source,temp,dest)
    result.append((source,dest))
    hanoi(n-1,temp,dest,source)

hanoi(n,1,3,2)
print(len(result))

for elem in result:
    print(elem[0],elem[1])
