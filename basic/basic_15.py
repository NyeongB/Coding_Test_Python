'''
출제 : 백준
난이도 : 실버3
문제 : N과 M(1)
날짜 : 21.03.24
유형 : 순열
'''

from itertools import permutations


n, r = map(int, input().split())

arr = []

for i in range(n):
    arr.append(i+1)

a = list(permutations(arr,r))

for i in a:
    for j in range(r):
        print(i[j], end=" ")
    print()


'''
순열 nPr 을 itertools로 라이브러리를 통해 구현해봤다.
'''

