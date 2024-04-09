import sys
num = 0
all_sum = 0

d = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

for _ in range(20):
    name, number, grade = sys.stdin.readline().split()
    if grade == "P":
        continue
    number = float(number)
    num += number
    all_sum += number * d[grade]
print(all_sum/num)
