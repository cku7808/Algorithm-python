apart = [[0]*14 for i in range(15)]
for i in range(15):
    for j in range(14):
        if i==0:
            apart[i][j] = j+1
        elif j==0:
            apart[i][j] = 1
        else:
            apart[i][j] = apart[i][j-1] + apart[i-1][j]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    print(apart[k][n-1])
    
