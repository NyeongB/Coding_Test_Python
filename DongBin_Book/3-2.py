'''
문제 : 큰 수의 법칙
날짜 : 21.03.17
유형 : Greedy
'''

n, m, k = map(int,input().split())

arr = list(map(int, input().split()))

arr.sort()

a = arr[-1]
b = arr[-2]

total = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        total += a
        m -= 1
    
    if m == 0:
        break
    m -= 1
    total += b

print(total)
        
'''
5 8 3
2 4 5 4 6
->46
'''            
    