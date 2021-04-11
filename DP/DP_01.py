'''
출제 : 백준
난이도 : 실버 3
문제 : 2xn 타일링
날짜 : 21.04.11
유형 : DP
'''

n = int(input())

dp = []
dp.append(1)
dp.append(2)

for i in range(2,n):
    dp.append(dp[i-2]%10007+dp[i-1]%10007)

print(dp[n-1]%10007)