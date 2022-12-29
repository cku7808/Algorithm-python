# A-Z : 65-90
# a-z : 97-122
# 0-9 : 15-24
def solution(s):
    s = s.lower()
    answer = ""
    for idx, elem in enumerate(s):
        if idx==0 or s[idx-1]==" ":
            if s[idx].isalpha():
                answer += s[idx].upper()
            else:
                answer += s[idx]
        else:
            answer += s[idx]
    return answer