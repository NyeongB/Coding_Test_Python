'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 큰 수 만들기
날짜 : 21.01.30
유형 : 그리디
'''

def solution(number, k):
    answer = ''
    index = -1
    
    for i in range(len(number) - k):
        max_num = 0
        for j in range(index+1, k+i+1):
            if max_num < int(number[j]):
                index = j
                max_num = int(number[j])
        answer += str(max_num)
    
    return answer

print(solution("1924",2))

'''
##8,10 시간초과##
java 내에서 이렇게 풀었는데 확실히 파이썬이 느리긴한가
다시 고민
'''