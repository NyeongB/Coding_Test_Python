'''
문제 : 개미 전사
날짜 : 21.05.08
유형 : Dynamic Programming
'''

n = int(input())

arr = list(map(int,input().split()))

dp = [0] * 100

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[n-1])

'''
확실히 DP 점화식 문제가 감이 와닿진않는다
처음 봤을때 완전 탐색 문제같기도했다
그리고 바텀업 초기 설정할때 왜 max를 넣는지도 몰랐는데 이건 
1 . . 3 이렇게 선택되는 경우가 있기 때문으로 이해하고 넘어간다.
'''