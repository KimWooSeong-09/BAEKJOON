user_input = int(input())
origin_num = user_input
cnt = 0

while True:
    ten = user_input // 10
    one = user_input % 10
    sum_num = ten + one

    user_input = (one * 10) + (sum_num % 10)
    cnt += 1

    if user_input == origin_num:
        break

print(cnt)
