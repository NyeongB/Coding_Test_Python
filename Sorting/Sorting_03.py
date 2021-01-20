'''
출제 : 백준
난이도 : 실버 5
문제 : 좌표 정렬하기 2
날짜 : 21.01.20
유형 : 정렬
'''

import functools

n = int(input())

array = []

def compa(a,b):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        if a[0] > b[0]:
            return 1
        else:
            return -1

array = [list(map(int,input().split())) for _ in range(n)]
array = sorted(array, key=functools.cmp_to_key(compa))

for i, j in array:
    print(i,j)

