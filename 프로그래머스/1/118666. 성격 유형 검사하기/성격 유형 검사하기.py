def solution(survey, choices):
    all_dict = {
        "RT":{"R":0, "T":0},
        "FC":{"C":0, "F":0},
        "MJ":{"J":0, "M":0},
        "NA":{"A":0, "N":0}
    }
    score = [0,3,2,1,0,1,2,3]
    
    for i in range(len(choices)):
        pointer = ""
        if survey[i] == "RT" or survey[i] == "TR":
            pointer = "RT"
        elif survey[i] == "FC" or survey[i] == "CF":
            pointer = "FC"
        elif survey[i] == "MJ" or survey[i] == "JM":
            pointer = "MJ"
        else:
            pointer = "NA"
            
        if choices[i] > 4:
            all_dict[pointer][survey[i][1]] += score[choices[i]]
        else:
            all_dict[pointer][survey[i][0]] += score[choices[i]]
    
    answer = ""
    for key in all_dict.keys():
        answer += max(all_dict[key].keys(), key=lambda x: all_dict[key][x])
    
    return answer

