
n = int(input())

<<<<<<< HEAD
    m = []
    print(hm)
    for k,v in hm.items():
        m.append(len(v))
=======
data = []
answer = []

for _ in range(n):
    data.append(int(input()))
>>>>>>> 09171ce575002c7d714cfea00f12140e8216d39a

def recursion(n,sum):
    if n < sum:
        return 0
    elif n == sum:
        return 1

    result = 0

<<<<<<< HEAD
print(solution(orders))
=======
    for i in range(1, 4):
        result += recursion(n,sum+i)
    
    return result

for i in data:
    answer.append(recursion(i,0))

for i in answer:
    print(i)
>>>>>>> 09171ce575002c7d714cfea00f12140e8216d39a
