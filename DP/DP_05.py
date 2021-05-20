'''
출제 : 백준
난이도 : 실버 2
문제 : 연속합
날짜 : 21.05.20
유형 : DP
'''

n = int(input())

a = list(map(int,input().split()))

for i in range(1,len(a)):
    a[i] = max(a[i],a[i]+a[i-1])

print(max(a))    