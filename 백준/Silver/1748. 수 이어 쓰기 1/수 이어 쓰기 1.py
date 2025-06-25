n = int(input())
length = 1
count = 0
start = 1

while start * 10 <= n:
    count += (start * 10 - start) * length
    start *= 10
    length += 1

count += (n - start + 1) * length
print(count)
