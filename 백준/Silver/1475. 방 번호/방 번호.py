user_input = input()

num_count = [0] * 10 

for i in user_input:
    num = int(i)
    if num == 6 or num == 9:
        num_count[6] += 1
    else:
        num_count[num] += 1

num_count[6] = (num_count[6] + 1) // 2

print(max(num_count))
