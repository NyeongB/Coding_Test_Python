'''
출제 : 백준
난이도 : 실버 5
문제 : 다리 놓기
날짜 : 21.04.04
유형 : 조합
'''

import math

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input())

answer = []

for _ in range(n):
    a, b = map(int, input().split())
    answer.append(math.factorial(b) // (math.factorial(a) * math.factorial(b-a) ) )

for i in answer:
    print(i)


'''
조합 nCr 을 itertools로 라이브러리를 통해 구현해봤다.
'''

