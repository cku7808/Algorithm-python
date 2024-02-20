import sys

p, m = map(int, sys.stdin.readline().split())

game = {}
room_cnt = 1
for _ in range(p):
    l, n = sys.stdin.readline().split()
    l = int(l)
    
    if len(game) == 0:
        game[f"room_num{room_cnt}"]= {"info":[(l,n)]}
        room_cnt += 1
    else:
        isentered = False
        for room in game:
            if len(game[room]["info"]) < m:
                if l <= game[room]["info"][0][0] + 10 and l >= game[room]["info"][0][0] - 10:
                    game[room]["info"].append((l,n))
                    isentered = True
                    break
        if not isentered:
            game[f"room_num{room_cnt}"]= {"info":[(l,n)]}
            room_cnt += 1

for room in game:
    game[room]["info"].sort(key=lambda x:x[1])
    if len(game[room]["info"]) == m:
        print("Started!")
        for v in game[room]["info"]:
            print(v[0],v[1])
    else:
        print("Waiting!")
        for v in game[room]["info"]:
            print(v[0],v[1])
