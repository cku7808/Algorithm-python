def solution(sizes):
    max_width, max_height = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        max_width = max(max_width, sizes[i][0])
        max_height = max(max_height, sizes[i][1])
    return max_width*max_height
            