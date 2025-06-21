hour_limit = 23
minute_limit = 60

H, M = map(int, input().split())
Cook_Time = int(input())

total = (H * minute_limit) + M + Cook_Time
H = total // minute_limit
M = total - (H * minute_limit)
if H > 23:
    H -= 24

print(H, M)