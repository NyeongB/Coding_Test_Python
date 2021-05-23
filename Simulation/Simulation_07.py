'''
출제 : 프로그래머스
난이도 : 레벨 2 
문제 : 방문 길이
날짜 : 21.05.23
유형 : 시뮬레이션
'''

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def solution(dirs):
    answer = 0
    x,y = 0,0
    visited = set()
    for idx in range(len(dirs)):
        dir = dirs[idx]
        i = -1
        if dir == 'U':
            i = 0
        elif dir == 'D':
            i = 1
        elif dir == 'L':
            i = 2
        elif dir == 'R':
            i = 3
        nx = x + dx[i]
        ny = y + dy[i]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x = nx
            y = ny
    
    answer = len(visited)//2
    return answer

'''
처음에 출발위치와 방향만 넣어서 하니깐 35점 나왔는데
저렇게 시작 도착, 도착, 시작을 넣고 //2를 해줘야 완성 
'''