'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 짝지어 제거하기
날짜 : 21.05.24
유형 : 스택
'''

def solution(s):
    answer = -1

    stack = []
    arr = list(s)
    
    for i in arr:
        if stack == []:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    
    if stack == []:
        answer = 1
    else:
        answer = 0

    return answer

'''
눈감고 풀었다.
'''