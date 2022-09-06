max_num = 0
max_index = 0
for i in range(9):
    n = int(input())
    if n > max_num :
        max_index = i+1
        max_num = n
print(max_num)
print(max_index)