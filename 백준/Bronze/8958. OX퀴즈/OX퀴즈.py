n = int(input())
for _ in range(n):
    s = input()
    result = 0
    pointer = 0
    
    for elem in s:
        if elem == 'X':
            pointer = 0
        else:
            pointer += 1
            result += pointer
    print(result)
