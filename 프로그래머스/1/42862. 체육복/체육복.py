def solution(n, lost, reserve):
    clothe = dict()
    answer = n
    for elem in reserve:
        if elem not in lost:
            clothe[str(elem)] = 2
            answer -= 1
            
    for elem in lost:
        if elem not in reserve:
            clothe[str(elem)] = 0
            answer -= 1


    for elem in sorted(lost):
        if elem not in reserve:
            if str(elem-1) in clothe and clothe[str(elem-1)] > 1:
                clothe[str(elem)] += 1
                clothe[str(elem-1)] -= 1
            elif str(elem+1) in clothe and clothe[str(elem+1)] > 1:
                clothe[str(elem)] += 1
                clothe[str(elem+1)] -= 1

    answer += sum(list(map(bool, clothe.values())))
    return answer
