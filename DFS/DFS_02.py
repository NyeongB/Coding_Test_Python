'''
출제 : 백준
난이도 : 골드5
문제 : 파이프 옮기기
날짜 : 21.01.14
유형 : DFS
'''
count = 0
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, direct):
    global count
    if x == n - 1 and y == n - 1:
        count += 1
        return

    # 가로 이동
    if direct == 0 or direct == 1:
        if y + 1 < n :
            if map[x][y+1] == 0 :
                dfs(x, y+1, 0)
    
    # 대각선 이동
    if direct == 0 or direct == 1 or direct == 2:
        if x + 1 < n and y + 1 < n :
            if map[x+1][y+1] == 0 and map[x+1][y] == 0 and  map[x][y+1] == 0:
                dfs(x+1, y+1, 1)


    # 세로 이동
    if direct == 1 or direct == 2:
        if x + 1 < n :
            if map[x+1][y] == 0:
                dfs(x+1, y, 2)



dfs(0,1,0)
print(count)