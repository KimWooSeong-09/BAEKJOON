N = int(input())
GroupWorldNumber = 0

for _ in range(N):
    words = input()
    used = []
    isGroupWord = True
    past_word = '' 

    for ch in words:
        if ch != past_word:
            if ch in used:
                isGroupWord = False
                break
            used.append(ch)
        past_word = ch  

    if isGroupWord:
        GroupWorldNumber += 1

print(GroupWorldNumber)
