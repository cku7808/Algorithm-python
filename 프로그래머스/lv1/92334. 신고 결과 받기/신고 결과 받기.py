# def solution(id_list, report, k):
#     answer = [0 for _ in range(len(id_list))] #메일횟수
#     num = [0 for _ in range(len(id_list))] #신고횟수
    
#     n_report = set(report) #중복제거
    
#     for elem in n_report: #신고당한 횟수
#         a, b = elem.split()
#         num[id_list.index(b)] += 1
    
#     for elem1 in id_list: #메일 받을 사람
#         for elem2 in n_report:
#             a, b = elem2.split()
#             if elem1 == a and num[id_list.index(b)] >= k:
#                 answer[id_list.index(a)] += 1
    
#     return answer

def solution(id_list, report, k):
    report_list = {}
    result = {}
    
    for ID in id_list:
        report_list[ID] = [0,[]]
        result[ID] = 0
    
    for info in report:
        reporter, reported = info.split() 
        if reporter not in report_list[reported][1]:
            report_list[reported][0] += 1
            report_list[reported][1].append(reporter)
            
    for key, val in report_list.items():
        if val[0] >= k:
            for reporter in val[1]:
                result[reporter] += 1
    return list(result.values())
            