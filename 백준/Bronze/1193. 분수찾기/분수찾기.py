x = int(input())

i = 1
while x>i:
    x -= i
    i+=1

if i%2==0:
    u = x
    d = i-x+1
else:
    u = i-x+1
    d = x
    
print(u,"/",d, sep="")

