'''
출제 : 백준
난이도 : 실버3
문제 : N과 M(2)
날짜 : 21.03.24
유형 : 조합
'''

from itertools import combinations


n, r = map(int, input().split())

arr = [i for i in range(1,n+1)] #리스트 내포 

combi = list(combinations(arr,r))

for i in combi:
    for j in range(r):
        print(i[j], end=' ')
    print()

'''
조합 nCr 을 itertools로 라이브러리를 통해 구현해봤다.
'''

