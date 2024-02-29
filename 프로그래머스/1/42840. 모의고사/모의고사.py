def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5]*len(answers)
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    
    num1 = num1[:len(answers)]
    num2 = num2[:len(answers)]
    num3 = num3[:len(answers)]
    
    arr = [num1, num2, num3]
    cnt = [0]*3
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == answers[j]:
                cnt[i] += 1
    
    max_cnt = max(cnt)
    for idx, elem in enumerate(cnt):
        if elem == max_cnt:
            answer.append(idx+1)
    return answer

                
        
                
        
    