import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    tpl = [tuple(map(int, input().split())) for _ in range(N)]

    tpl.sort()
    
    cnt = 1  
    b_i = tpl[0][1]
    
    for i in range(1, N):
        if tpl[i][1] < b_i:
            cnt += 1
            b_i = tpl[i][1]
    
    print(cnt)
