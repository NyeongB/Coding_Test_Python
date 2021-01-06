'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 올바른 괄호
날짜 : 21.01.06
유형 : 스택
'''

def solution(s):
    answer = True
    stack = list()  #파이썬에선 리스트로 스택
    
    for i in range(0,len(s)) :
        if s[i]=="(":
            stack.append("(")
        else :
            if len(stack) !=0:
                stack.pop()
            else : 
                answer = False
                break
    
    if len(stack) != 0 :
        answer = False

    return answer

#테스트
print(solution("(())"))
print(solution("(())("))

'''
아직은 쉬운 문제로 파이썬 적응해 나가야할 것 같다.
'''