'''
출제 : 백준
난이도 : 실버 1
문제 : 그림
날짜 : 21.05.09
유형 : BFS
'''
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs(x, y):
    ans = 1
    q = deque()
    q.append((x,y))
    arr[x][y] = 2

    while q :
        x, y = q.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 2
                    q.append((nx, ny))
                    ans += 1
                    
    return ans


n, m = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n) )
count = 0
result = [0]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            result.append(bfs(i,j))
            count += 1

print(count)
print(max(result))

'''
처음 런타임 에러가 났다
원인은 모든게 0 으로 들어가면 
기존 result 리스트에 0조차도 안들어가서 
아무것도 없는 list에 max값을 호출하니깐 런타임이 뜬거였다.
쉽다 생각해도 방심하지 말아라..
'''