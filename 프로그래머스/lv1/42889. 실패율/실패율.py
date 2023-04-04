def solution(N, stages):
    fail = [0]*N
    stages.sort() #12223346
    probs = list(set(stages))#12346
    for prob in range(1,N+1):
        chal = 0
        yet = 0
        for stage in stages:
            if stage >= prob:
                chal += 1
            if stage == prob:
                yet += 1

        if chal == 0:
            fail[prob-1] = [prob, 0]
            continue
        fail[prob-1] = [prob,yet/chal]

    fail = sorted(fail, key=lambda x:x[1],reverse=True)
    answer = []
    for elem in fail:
        answer.append(elem[0])

    return answer