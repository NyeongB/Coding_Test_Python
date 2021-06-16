'''
난이도 : 레벨 2
문제 : 더 맵게
날짜 : 21.06.16
유형 : 힙
'''
import heapq as h

def solution(s, K):
    answer = 0
    
    h.heapify(s)
    
    while True:
        first = h.heappop(s)
        
        if first >= K:
            break
        
        if len(s) == 0:
            answer = -1
            break
        
        second = h.heappop(s)
        h.heappush(s,first + 2*second)
        answer += 1
    
    return answer
