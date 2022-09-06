a, b = input().split()
na = ''
nb = ''
for i in range(2,-1,-1):
    na += a[i]
    nb += b[i]
    
print(max(int(na), int(nb)))
