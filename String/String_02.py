'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 가장 큰 수
날짜 : 21.01.07
유형 : 문자열
'''

import functools

def comparator(a ,b):   #comparator 정의해서 사용
    str1 = a + b
    str2 = b + a
    a = int(str1)
    b = int(str2)
    
    if a > b :
        return 1
    elif a < b :
        return -1
    else :
        return 0

def solution(numbers):
    n = [str(i) for i in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int("".join(n)))   # "0000" 나올수도 있어서 int변환후 str변환
    return answer

'''
import functools
def 함수 :
key=functools.cmp_to_key(함수)
'''