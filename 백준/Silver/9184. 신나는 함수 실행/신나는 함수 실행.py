import sys,itertools

n = [i for i in range(21)]
nums = list(itertools.product(n, repeat=3))

result = dict()

for elem in nums:
    if elem[0]<=0 or elem[1]<=0 or elem[2]<=0:
        result[elem] = 1
    else:
        a = elem[0]
        b = elem[1]
        c = elem[2]
        if a<b and b<c:
            ans = result[(a,b,c-1)]+result[(a,b-1,c-1)]-result[(a,b-1,c)]
            result[elem] = ans
        else:
            ans = result[(a-1,b,c)]+result[(a-1,b-1,c)]+result[(a-1,b,c-1)]-result[(a-1,b-1,c-1)]
            result[elem] = ans

while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        print("w("+str(a)+", "+str(b)+", "+str(c)+") =",1)
    elif a>20 or b>20 or c>20:
        print("w("+str(a)+", "+str(b)+", "+str(c)+") =",result[(20,20,20)])
    else:
        print("w("+str(a)+", "+str(b)+", "+str(c)+") =",result[(a,b,c)])
