'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 다음 큰 숫자
날짜 : 21.01.07
유형 : 
'''

def solution(n):
    answer = 0
    count = bin(n).count("1")
    for i in range(n + 1, 1000001):
        if bin(i).count("1") == count:
            answer = i
            break
    return answer

# 테스트
print(solution(78))

'''
bin() 함수사용하여 문자열 형태로 2진법 변환후에 count함수를 사용하여 문자열내에 1의 갯수를 센다
1의 갯수가 같은 다음 큰숫자를 출력
'''