'''
출제 : 프로그래머스
난이도 : 레벨2
문제 : 숫자의 표현
날짜 : 21.01.26
유형 : 
'''
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        total = 0
        while True:
            total += i
            i +=1
            if n<= total:
                break
        if total == n:
            answer +=1
    
    
    return answer

print(solution(15))

'''
n이 10000까지여서 완전 탐색으로 풀었다.
'''