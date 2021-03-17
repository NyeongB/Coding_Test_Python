'''
문제 : 거스름돈
날짜 : 21.03.17
유형 : Greedy
'''

N = int(input())

count = 0

coins = [500, 100, 50, 10]

for i in coins:
    count += int((N / i))
    N %= i

print(count)