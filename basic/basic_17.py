'''
출제 : 백준
난이도 : 골드 5
문제 : 암호 만들기
날짜 : 21.04.04
유형 : 조합
'''
# 4 6
# a t c i s w

from itertools import combinations

c, n = map(int, input().split())

alpha = list(input().split())
alpha.sort()

result = list(combinations(alpha, c))

for i in result:
    count = 0
    count2 = 0
    for j in i :
        if j in 'aeiou':
            count += 1
        else :
            count2 += 1
    if count < 1:
        continue
    if count2 < 2:
        continue
    print("".join(i))


'''
조합 nCr 을 itertools로 라이브러리를 통해 구현해봤다.
'''

