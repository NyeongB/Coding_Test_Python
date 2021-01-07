'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 전화번호 목록
날짜 : 21.01.07
유형 : 
'''

def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i==j:
                continue
            if phone_book[j].find(phone_book[i]) == 0:
                return False
    
    return answer

# 테스트
print(solution(["119", "97674223", "1195524421"]))

'''
find라는 문자열 함수를 사용하였다
'''