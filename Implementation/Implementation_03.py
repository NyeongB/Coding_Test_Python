'''
출제 : 백준
난이도 : 실버 3
문제 : 배열 돌리기 1
날짜 : 21.04.08
유형 : 구현
'''

n, m, r = map(int, input().split())

arr = list( list(map(int, input().split())) for _ in range(n) )

s = min(n,m) // 2

d = [(0,1),(1,0),(0,-1),(-1,0)]

# rotate function
def rotate(s):

    for i in range(s):
        dir = 0
        x = i
        y = i
        value = arr[i][i]
        while dir < 4:
            dx = x + d[dir][0]
            dy = y + d[dir][1]
            if dx>=i and dy>=i and dx<n-i and dy<m-i:
                arr[x][y] = arr[dx][dy]
                x = dx
                y = dy
            else:
                dir += 1
        arr[i+1][i] = value

# rotate
for _ in range(r):
    rotate(s)


# print
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()


'''
어렵다.. 익숙해지자.. 
원리 파악하느라 힘들었다
비슷한 유형 문제 계속 풀자
'''