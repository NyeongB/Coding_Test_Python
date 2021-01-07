'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 124 나라
날짜 : 21.01.07
유형 : 
'''

def solution(n):
    num = ["1", "2", "4"]
    answer = ""
    
    while n>0:
        n -= 1
        answer = num[n%3] + answer
        n = n // 3
    return answer

# 테스트
print(solution(6))

'''
아직은 쉬운 문제로 파이썬 적응해 나가야할 것 같다.
'''