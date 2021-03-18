'''
문제 : 숫자 카드 게임
날짜 : 21.03.18
유형 : Greedy
'''

n, m = map(int, input().split())

result = 0

for _ in range(n):
    x = min(list(map(int, input().split())))

    result = max(result, x)

print(result)

'''
2 4
7 3 1 8
3 3 3 4
-> 3
'''