'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 구명 보트
날짜 : 21.01.11
유형 : 그리디
'''

def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people) - 1
    
    while start < end :
        if people[start] + people[end] <= limit :
            start += 1
        
        end -= 1
        answer += 1
    if start == end :
        answer += 1
        
        
    return answer

print(solution([50,50,70,80],100))

'''
핵심은 정렬후에 start인덱스와 end 인덱스를 리미트와 비교해가며
보트의 갯수를 늘려감
'''