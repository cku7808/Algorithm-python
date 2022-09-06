arr = []
for _ in range(10):
    n = int(input())
    arr.append(n%42)

result = []
for elem in arr:
    if elem not in result:
        result.append(elem)
print(len(result))
