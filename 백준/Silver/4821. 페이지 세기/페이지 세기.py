result = []

while True:
    N = int(input())
    if N <= 0:
        break

    page_input = input()
    pages = set()

    for part in page_input.split(','):
        try:
            if '-' in part:
                low, high = part.split('-')
                low = int(low)
                high = int(high)

                if low > high:
                    continue
            else:
                low = high = int(part)

            for page in range(low, high + 1):
                if 1 <= page <= N:
                    pages.add(page)
        except:
            continue  

    result.append(len(pages))

for res in result:
    print(res)
