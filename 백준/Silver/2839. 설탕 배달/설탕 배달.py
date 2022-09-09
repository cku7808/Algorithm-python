n = int(input())
result = []

for i in range(n//5+1):
    f = 5*i
    t = (n-f)//3
    if (n-f)%3 == 0 or n-f==0:
        result.append(i+t)
if len(result)==0:
    ans = -1
else:
    ans = min(result)
print(ans)
