import sys

n = int(sys.stdin.readline())

name_dict = {"ChongChong" : True}

cnt = 1
for _ in range(n):
    name1, name2 =  sys.stdin.readline().strip().split()

    if name1 not in name_dict:
        name_dict[name1] = False
    if name2 not in name_dict:
        name_dict[name2] = False

    if name_dict[name1] and not name_dict[name2]:
        name_dict[name2] = True
        cnt += 1
    elif name_dict[name2] and not name_dict[name1]:
        name_dict[name1] = True
        cnt += 1
print(cnt)
        
            
