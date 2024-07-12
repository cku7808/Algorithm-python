n = int(input())

result = []
for i in range(1,n+1):
    cnt = 0
    for s in str(i):
        if s in ["3","6","9"]:
            cnt += 1
    if cnt > 1:
        result.append("--")
    elif cnt > 0 :
        result.append("-")
    else:
        result.append(str(i))

print(" ".join(result))
