import sys

user_num = int(sys.stdin.readline())
count = [0] * 10001 

for _ in range(user_num):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
