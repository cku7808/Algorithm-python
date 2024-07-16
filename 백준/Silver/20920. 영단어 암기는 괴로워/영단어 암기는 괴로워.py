import sys

n ,m = map(int, sys.stdin.readline().split())

word_dict = dict()
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        try:
            word_dict[word][0] += 1
        except:
            word_dict[word] = [1,len(word), word]
            
tmp = sorted(word_dict.values(), key=lambda x: (-x[0], -x[1], x[2]))

for elem in tmp:
    print(elem[-1])
