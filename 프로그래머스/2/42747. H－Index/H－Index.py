def solution(citations):
    max_cite = max(citations)
    citations.sort()
    answer = 0
    for i in range(max_cite):
        cnt = 0
        for elem in citations:
            if elem >= i:
                cnt += 1
        if cnt <= i:
            answer = max(cnt, answer)
    return answer
            