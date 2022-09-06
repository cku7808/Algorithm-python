s = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for elem1 in s:
    for i in range(len(dial)):
        if elem1 in dial[i]:
            result += i+3
            
print(result)
