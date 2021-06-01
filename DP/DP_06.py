'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 피보나치 수
날짜 : 21.06.01
유형 : DP
'''

def solution(num):
    answer = [0,1]

    for i in range(2,num+1):
        answer.append((answer[i-1]+answer[i-2])% 1234567)
    

    return answer[-1]