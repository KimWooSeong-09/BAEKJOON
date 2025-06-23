user_input = int(input())
Gandalf_list = [1, 2, 3, 3, 4, 10]
Sauron_list = [1, 2, 2, 2, 3, 5, 10]
result = []

for i in range(user_input):
    Gandalf = 0
    Sauron = 0
    Gandalfs = list(map(int, input().split()))
    Saurons = list(map(int, input().split()))
    for j in range(6):
        Gandalf += Gandalfs[j] * Gandalf_list[j]
    for k in range(7):
        Sauron += Saurons[k] * Sauron_list[k]
    if Gandalf > Sauron:
        result.append(f'Battle {i + 1}: Good triumphs over Evil')
    elif Gandalf < Sauron:
        result.append(f'Battle {i + 1}: Evil eradicates all trace of Good')
    else:
        result.append(f'Battle {i + 1}: No victor on this battle field')

for i in range(user_input):
    print(result[i])