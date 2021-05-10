'''
출제 : 백준
난이도 : 실버 3
문제 : 1로 만들기
날짜 : 21.05.08
유형 : DP
'''

n = int(input())

dp = [0] * (10**6+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

'''
동빈북에서 풀었던 비슷한문제 
바텀업 방식으로 문제를 해결해 나간다.
'''