'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 가장 큰 수
날짜 : 21.06.20
유형 : 정렬
'''
import functools

def comparator(a, b):
    i = int(str(a) + str(b))
    j = int(str(b) + str(a))
    
    if i < j:
        return 1
    elif i > j:
        return -1
    else:
        return 0

def solution(numbers):
    answer = ''
    numbers.sort(key=functools.cmp_to_key(comparator))
    for i in numbers:
        answer += str(i)
    return str(int(answer))

'''
중요한거 위주로
'''