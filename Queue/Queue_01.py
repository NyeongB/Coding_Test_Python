'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 프린터
날짜 : 21.01.07
유형 : 큐
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([(v,i) for i, v in enumerate(priorities)])
    
    while len(queue)>0 :
        temp = queue.popleft()
        if queue and temp[0] < max(queue)[0] :
            queue.append(temp)
        else :
            answer += 1
            if temp[1]==location :
                break
            
    
    return answer

print(solution([1, 1, 9, 1, 1, 1],0))

'''
queue = deque([(v,i) for i, v in enumerate(priorities)])
이런식으로 리스트의 인덱스와 값을 한번에 쌍으로 큐에 담을 수 있다.
'''