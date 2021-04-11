
n = int(input())

data = []
answer = []

for _ in range(n):
    data.append(int(input()))

def recursion(n,sum):
    if n < sum:
        return 0
    elif n == sum:
        return 1

    result = 0

    for i in range(1, 4):
        result += recursion(n,sum+i)
    
    return result

for i in data:
    answer.append(recursion(i,0))

for i in answer:
    print(i)