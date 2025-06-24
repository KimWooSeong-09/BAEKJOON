number = list(range(1, 9))

user_input = list(map(int, input().split()))

ascending = 0
descending = 0
mixed = 0

for i in range(8):
    if number[i] == user_input[i]:
        ascending += 1
    elif number[(i + 1) * -1] == user_input[i]:
        descending += 1
    else:
        mixed += 1
if ascending == 8:
    print("ascending")
else:
    mixed += ascending
if descending == 8:
    print("descending")
else:
    mixed += descending
if mixed == 8:
    print("mixed")