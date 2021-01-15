'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 더 맵게
날짜 : 21.01.15
유형 : 우선순위 큐
'''

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) ==0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        answer += 1
    
    return answer

'''

'''