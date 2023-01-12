def solution(genres, plays):
    playlist = dict()
    for i in range(len(plays)):
        if genres[i] in playlist:
            playlist[genres[i]].append([plays[i],i])
            playlist[genres[i]] = sorted(playlist[genres[i]],key=lambda x:x[0],reverse=True)
        else:
            playlist[genres[i]] = [[plays[i],i]]
            
    result = []     
    for key, value in playlist.items():
        tmp = 0
        for n, idx in value:
            tmp += n
        result.append([key,tmp])
    result = sorted(result, key=lambda x:x[1], reverse=True)
    
    answer = []
    for genre, total in result:
        if len(playlist[genre]) < 2:
            answer.append(playlist[genre][0][1])
        else:
            answer.append(playlist[genre][0][1])
            answer.append(playlist[genre][1][1])
    return answer