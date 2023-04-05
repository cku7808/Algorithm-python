import re

def solution(files):
    mod_files = []
    comp_char = re.compile('[a-z\-\. ]',re.I)
    comp_num = re.compile('[0-9]')
    
    for i in range(len(files)):
        head, number, tail = "","",""
        
        for j in range(len(files[i])):
            if comp_char.match(files[i][j]) and number == "":
                head += files[i][j]
            elif comp_num.match(files[i][j]):
                number += files[i][j]
            elif number != "" and comp_char.match(files[i][j]):
                tail = files[i][len(head)+len(number):]
                break

        mod_files.append((head,number,tail))
    mod_files = sorted(mod_files, key = lambda x:(x[0].lower(),int(x[1])))
    
    answer = [h+n+t for h,n,t in mod_files]
    return answer
