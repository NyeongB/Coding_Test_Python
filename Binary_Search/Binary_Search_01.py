'''
출제 : 백준
난이도 : 실버 3
문제 : 나무자르기
날짜 : 21.01.22
유형 : 이분 탐색
'''
import sys

n, target = map(int, sys.stdin.readline().rstrip().split() )

a = list(map(int,sys.stdin.readline().rstrip().split()  ))
a.sort()
s = 0
e = max(a)
result = 0

while s<=e:
    mid = (s+e) // 2
    t = 0
    for i in a:
        if i - mid > 0:
            t += i - mid
    
    if target > t:
        e = mid - 1
    else:
        s = mid + 1
        result = mid


print(result)