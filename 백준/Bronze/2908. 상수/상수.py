N, M = map(int, input().split())
    
if int(str(N)[::-1]) > int(str(M)[::-1]):
    print(int(str(N)[::-1]))
else:
    print(int(str(M)[::-1]))