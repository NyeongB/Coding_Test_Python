'''
출제 : 백준
난이도 : 실버 1
문제 : 미로 탐색
날짜 : 21.01.11
유형 : BFS
'''
n, m = map(int,input().split())
map = [list( map(  int, list(input()) )  ) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x, y):
    queue = [[x,y]]

    while queue :
        temp = queue.pop(0)
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if nx >= 0 and ny >=0 and nx < n and ny < m :
                if map[nx][ny] == 1 :
                    map[nx][ny] += map[temp[0]][temp[1]]
                    queue.append([nx,ny])

bfs(0,0)
print(map[n-1][m-1])





