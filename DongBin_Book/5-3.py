# 21.01.16
# p.149
# 음료수 얼려 먹기

n, m = map(int, input().split())
a = []
cnt = 0
for _ in range(n):
    a.append(list(map(int, input())))

def dfs(x, y) :
    if 0<=x<n and 0<=y<m:
        if a[x][y] ==0 :
            a[x][y] = 1
            dfs(x,y+1)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x-1,y)
    
    return


for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000000011100
11111111111001
11110001111111
11110000111111
8
'''