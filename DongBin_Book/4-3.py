# 21.01.14
# p.120

n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [([False]*m) for _ in range(n)] 

dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 0
result = 1
visited[x][y] = True
print(map)
print(visited)

while True :
    if count == 4 :
        d = (d + 2) % 4
        nx = dx[d] + x
        ny = dy[d] + y
        d = (d + 2) % 4
        if (nx<0 or nx>=n or ny<0 or ny>=n):
            break
        if visited[nx][ny] == True or map[nx][ny] == 1 :
            break
        count = 0
        continue
    # 방향 회전
    count += 1
    d = (d + 3) % 4
    nx = dx[d] + x
    ny = dy[d] + y
    if (nx<0 or nx>=n or ny<0 or ny>=n):
        continue
    if visited[nx][ny] == True or map[nx][ny] == 1 :
        continue
    x = nx
    y = ny
    visited[x][y] = True
    count = 0
    result += 1

print(result)

'''
로봇 청소기랑 비슷한 문제
'''