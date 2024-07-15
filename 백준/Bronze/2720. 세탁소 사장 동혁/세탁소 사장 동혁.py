import sys

t = int(sys.stdin.readline())

for _ in range(t):
    coin = int(sys.stdin.readline())
    
    coin_type = [0, 0, 0, 0]

    for idx, div_coin in enumerate([25, 10, 5, 1]):
        coin_type[idx] += coin//div_coin
        coin %= div_coin
    print(*coin_type)
