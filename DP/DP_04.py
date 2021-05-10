'''
출제 : 백준
난이도 : 실버 3
문제 : 피보나치는 지겨웡~
날짜 : 21.05.10
유형 : DP
'''

n = int(input())

dp = [0] * 51

dp[0] = dp[1] = 1

if n >=2:
    for i in range(2, n+1):
        dp[i] = (1 + dp[i-1] + dp[i-2]) % 1000000007

print(dp[n])