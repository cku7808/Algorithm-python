s1 = int(input())
s2 = input()

for i in range(len(s2)-1, -1, -1):
    print(s1*int(s2[i]))
print(s1*int(s2))