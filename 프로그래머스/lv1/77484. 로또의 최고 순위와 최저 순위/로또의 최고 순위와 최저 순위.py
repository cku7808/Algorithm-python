def solution(lottos, win_nums):   
    score = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    
    num = 0
    z_num = lottos.count(0)
    flag = [False for _ in range(6)]
    for elem1 in lottos:
        for elem2 in win_nums:
            if elem1 == elem2 and flag:
                num += 1

    best = z_num+num
    worst = num
    
    answer = [score[best], score[worst]]
    
    
    
    return answer