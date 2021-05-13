'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 배달
날짜 : 21.05.13
유형 : BFS
'''
from collections import deque

def solution(N, road, K):
    answer = 0

    distance = [1e9] * (N + 1)
    maps = list([0]*(N+1) for _ in range(N+1))
    
    for x,y,r in road:
        
        if maps[x][y] ==0:
            maps[y][x] = maps[x][y] = r
        else:
            maps[x][y] = maps[y][x] = min(maps[x][y],r)
    print(maps)        
    q = deque()
    
    q.append(1)
    distance[1] = 0
    while q:
        x = q.popleft()
        
        for y in range(1, N+1):
            if maps[x][y] != 0:
                if distance[y] > maps[x][y] + distance[x] and maps[x][y] + distance[x] <= K:
                    distance[y] = distance[x] + maps[x][y]
                    q.append(y)
    answer = len([i for i in distance if i <= K])
    return answer


print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))

'''
방문 누적값 정리
'''