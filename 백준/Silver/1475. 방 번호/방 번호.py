import sys, math

n = sys.stdin.readline().strip()

d = {}
for elem in "012345678":
    d[elem] = 0

for elem in n:
    if elem == "9":
        d["6"] += 1
    else:
        d[elem] += 1

d["6"] = math.ceil(d["6"]/2)
print(max(d.values()))
        
