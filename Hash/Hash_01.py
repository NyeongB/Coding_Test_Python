'''
출제 : 프로그래머스
난이도 : 레벨 1
문제 : 완주하지 못한 선수
날짜 : 21.01.05
유형 : 해시
'''

def solution(participant, completion):
    answer = ''
    dict = {}
    for i in participant:
        if dict.get(i) == None :
            dict[i] = 1;
        else :
            dict[i] = dict.get(i) + 1
            
    for i in completion :
        dict[i] = dict.get(i) - 1
        
    for i in participant:
        if dict[i] ==1 :
            answer = i
    
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))

'''
파이썬에는 딕셔너리라는 자료형이 존재
hash()랑 함께 쓰이는것같음
하지만 기본적인 해시 구조로 풀어봄
'''