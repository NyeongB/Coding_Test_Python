'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 가장 큰 수
날짜 : 21.05.26
유형 : 정렬
'''
import functools

def comparator(a, b):
    num1 = int( str(a) + str(b) )
    num2 = int( str(b) + str(a) )
    
    if num2 > num1:
        return 1
    elif num1 > num2:
        return -1
    else:
        return 0

def solution(numbers):
    answer = ''
    numbers.sort(key=functools.cmp_to_key(comparator))
    for i in numbers:
        answer += str(i)
    
    return str(int(answer))