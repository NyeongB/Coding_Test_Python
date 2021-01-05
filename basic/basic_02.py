'''
출제 : 프로그래머스
난이도 : 레벨 1
문제 : 문자열 내 p와 y의 개수
날짜 : 21.01.05
유형 : 
'''

def solution(s):
    s = s.lower()
    p_num = s.count("p")
    y_num = s.count("y")
    
    if p_num == y_num :
        return True
    else : 
        return False

result = solution("pPoooyY")
print(result)

'''
확실히 자바보다 간결하고 속도도 빠르다
'''