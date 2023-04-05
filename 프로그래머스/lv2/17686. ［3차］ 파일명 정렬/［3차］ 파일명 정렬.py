import re

# def solution(files):
#     mod_files = []
#     comp_char = re.compile('[a-z\-\. ]',re.I)
#     comp_num = re.compile('[0-9]')
    
#     for i in range(len(files)):
#         head, number, tail = "","",""
        
#         for j in range(len(files[i])):
#             if comp_char.match(files[i][j]) and number == "":
#                 head += files[i][j]
#             elif comp_num.match(files[i][j]):
#                 number += files[i][j]
#             elif number != "" and comp_char.match(files[i][j]):
#                 tail = files[i][len(head)+len(number):]
#                 break

#         mod_files.append((head,number,tail))
#     mod_files = sorted(mod_files, key = lambda x:(x[0].lower(),int(x[1])))
    
#     answer = [h+n+t for h,n,t in mod_files]
#     return answer


def solution(files):
    result = []
    for file in files:
        first_num = re.findall(r"\d+", file)[0]
        first_num_pos = file.index(first_num)
        head = file[:first_num_pos]
        number = file[len(head):len(head)+len(first_num)]
        tail = file[len(number)+len(head):]
        
        result.append((head,number,tail))
    result = sorted(result, key=lambda x:(x[0].lower(),int(x[1])))
    answer = [h+n+t for h,n,t in result]
    return answer


# 강사님 코드
# def solution(files):
#     answer = []
#     my_files = []
#     for idx, s in enumerate(files):
#         number = re.findall(r"\d+",s)
#         real_number = int(number[0])
#         head = s[:s.index(number[0])]
#         head = head.lower()
#         my_files.append([head,real_number,idx])
#     my_files.sort(key=lambda x:(x[0],x[1],x[2]))
#     answer = [ files[ j[2] ] for j in my_files ]
    
#     return answer
        