'''
출제 : 프로그래머스
난이도 : 레벨 1
문제 : 모의고사
날짜 : 21.01.08
유형 : 
'''

def solution(answers):
    count = [0] * 3
    answer = []
    su_1 = [1, 2, 3, 4, 5]
    su_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, num in enumerate(answers):
        if num == su_1[i % len(su_1)] :
            count[0] += 1
        if num == su_2[i % len(su_2)] :
            count[1] += 1
        if num == su_3[i % len(su_3)] :
            count[2] += 1
        
    for i, num in enumerate(count):
        if max(count) == num :
            answer.append(i+1)
            
    return answer

# 테스트
print(solution([1,3,2,4,2]))

'''
for문으로 인덱스와 값이 한번에 사용할 수 있는점이 좋고
리스트 자체에서 맥스값을 가져와 쉽게 사용할 수 있다.
'''