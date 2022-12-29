def solution(s):
    s = list(map(int,s.split()))
    answer = ""
    min_num = min(s)
    max_num = max(s)
    answer += str(min_num)+" "+str(max_num)
    return answer