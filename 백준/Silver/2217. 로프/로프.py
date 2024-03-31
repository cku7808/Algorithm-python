import sys

n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]

rope.sort()

answer = 0
for idx, elem in enumerate(rope):
    answer = max(answer, (n-idx)*elem)
print(answer)
