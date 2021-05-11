'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 게임 맵 최단거리
날짜 : 21.05.11
유형 : BFS
'''
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0,1))
    
    while q:
        x, y, r = q.popleft()
        if (x,y) == (n-1, m-1):
            answer = r
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    q.append((nx,ny,r+1))
                    maps[nx][ny] = 0
        
        
    
    return answer

'''
bfs 기본 문제
갈수록 정교해지는 느낌이 든다

'''