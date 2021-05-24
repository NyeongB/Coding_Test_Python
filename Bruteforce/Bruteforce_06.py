'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 수 이어가기
날짜 : 21.05.24
유형 : 브루트포스
'''
from itertools import permutations

def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = list(numbers)
    ans = list(permutations(arr,1))
    for i in range(2,len(numbers)+1):
        ans += list(permutations(arr,i))
    s = set()
    for i in ans:
        s.add(int(''.join(i)))
    
    for i in s:
        if prime(i):
            answer += 1
    
    
    return answer