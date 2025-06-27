board = []
current_place = 1
cnt = 0

N, M = map(int, input().split())

for _ in range(N):
    board.append(int(input()))

for _ in range(M):
    move = int(input())
    current_place += move
    cnt += 1
    if current_place >= N:
        break
    current_place += board[current_place - 1]
    if current_place >= N:
        break

print(cnt)
