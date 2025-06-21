def factorial(n): # 팩토리얼
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def combination(n, r): # 집합
    return factorial(n) // (factorial(r) * factorial(n - r))

# Main
result = []
user_input = int(input())
for _ in range(user_input):
    N, M = map(int, input().split())
    result.append(combination(M, N))

for i in range(user_input):
    print(result[i])  
