'''
출제 : 프로그래머스
난이도 : 레벨1
문제 : 핸드폰 번호 가리기
날짜 : 21.02.01
유형 : 
'''
def solution(phone_number):
    answer = ''
    l = len(phone_number) - 4
    for _ in range(l):
        answer += '*'
    answer +=phone_number[-4:]
    return answer