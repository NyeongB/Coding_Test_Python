'''
출제 : 백준
난이도 : 실버 2
문제 : 부분수열의 합
날짜 : 21.04.11
유형 : 순열
'''

from itertools import combinations

n, s = map(int, input().split())

arr = list(map(int, input().split()))
a = []

for i in range(1,len(arr)+1):
    a.extend(list(combinations(arr, i)))

count = 0

for i in a:
    if sum(i) == s:
        count+=1

print(count)


'''
조합으로 해봄
근데 파이썬만 쓰니깐 멍청이 되는느낌..
'''

