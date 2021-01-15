'''
출제 : 백준
난이도 : 골드 5
문제 : 뿌요뿌요
날짜 : 21.01.15
유형 : BFS
'''
from collections import deque

def bfs(x, y, cnt) :
    visited = [([False] * 6 ) for _ in range(12)]
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    flag = 1

    while q :
        temp = q.popleft()
        for i in range(4):
            nx = dx[i] + temp[0]
            ny = dy[i] + temp[1]

            if nx>=0 and ny>=0 and nx<12 and ny < 6:
                if not visited[nx][ny] and map[nx][ny] == map[temp[0]][temp[1]] : 
                    visited[nx][ny] = True
                    flag += 1
                    q.append([nx, ny])
    
    if flag >= 4:
        cnt += 1
        for i in range(12):
            for j in range(6):
                if visited[i][j] :
                    map[i][j] = '.'

    return cnt

def check_fall():
    for i in range(10, -1, -1):
        for j in range(6):
            if map[i][j] != '.' and map[i+1][j] == '.':
                for k in range(i+1, 12):
                    if k == 11 and map[k][j] == '.':
                        map[k][j] = map[i][j]
                    elif map[k][j] != '.':
                        map[k-1][j] = map[i][j]
                        break
                map[i][j] = '.'


dx = [1,-1,0,0]
dy = [0,0,1,-1]
map = []
for _ in range(12):
    map.append(list(input()))                

answer = 0

# 실행 
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if map[i][j] !='.' :
                cnt += bfs(i,j,cnt)

    if cnt == 0:
        print(answer)
        break
    else:
        answer +=1
        check_fall()

'''
핵심은 전체를 탐색하며 bfs로 4개이상 터트리기 + 그후에 떨구기 
터트린게 한번도 없다? -> 종료
'''


            
    
                  




