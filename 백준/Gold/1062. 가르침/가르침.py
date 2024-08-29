import sys

def check(word, comb):
    for i in range(26):
        if word[i] == 1 and comb[i] == 0:
            return False
    return True

def backtrack(idx, cnt):
    global max_ans
    # 최대 k-5개의 문자들을 가지고 부분 집합 구성
    if cnt == k-5:
        ans = 0
        for elem in words:
            if check(elem, comb):
                ans += 1
        max_ans = max(max_ans, ans)
        return

    for i in range(idx, 26):
        if candidates[i] and not comb[i]:
            comb[i] = 1
            backtrack(i+1, cnt+1)
            comb[i] = 0

n, k = map(int, sys.stdin.readline().split())
words = []
candidates = [0] * 26
comb = [0] * 26
for i in range(n):
    tmp = [0] * 26
    word = list(set(sys.stdin.readline().strip()) - {"a", "n", "t", "i", "c"})
    for w in word:
        tmp[ord(w)-ord("a")] = 1
        candidates[ord(w) - ord("a")] = 1
    words.append(tmp)

max_ans = 0

if k >= 5:
    if sum(candidates) < k - 5:
        max_ans = n
    else:
        backtrack(0, 0)

print(max_ans)