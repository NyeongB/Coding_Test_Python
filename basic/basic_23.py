'''
출제 : 백준
난이도 : 실버 3
문제 : 수 이어 쓰기 1
날짜 : 21.04.11
유형 : 수학
'''

n = input()

l = len(n)

count = 0

# 자리전 전까지는 확정 9 * 1, 99 * 2, 999 * 3 .... 
for i in range(0,l-1):
    count += 9* (10**i) * (i+1)

# 나머지 것들 자리수 곱해서 더하기 
count += (int(n) - (10**(l-1)) + 1)*l

print(count)