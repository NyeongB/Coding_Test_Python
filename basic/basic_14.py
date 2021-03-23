'''
출제 : 백준
난이도 : 실버1
문제 : 카잉 달력
날짜 : 21.03.23
유형 : 
'''


result = []

T = int(input())

for _ in range(T):
    flag = True
    m, n, x, y = map(int, input().split())

    while x <= m*n:
        if x % n == y % n :
            result.append(x)
            flag = False
            break
        x = x + m

    if flag:
        result.append(-1)


for i in result:
    print(i)


'''
처음 바로 시간초과
브루트 포스로 접근하면 최대 경우의수가 1초를 초과한다 40,000 * 40,000
답지보고 디버깅하면서 흐름만 이해..
'''

'''
T = int(input())

result = []

def caing(n,m,x,y):
    count = 1
    dx = 1
    dy = 1

    while True:
        #print(dx,dy)
        if dx == x and dy == y:
            return count

        if dx == n and dy == m:
            count += 1
            break

        if dx < n and dy < m :
            dx = dx + 1
            dy = dy + 1
        elif dx >= n and dy >= m :
            dx = 1
            dy = 1
        elif dx >= n :
            dx = 1
            dy = dy + 1
        elif dy >= m :
            dy = 1     
            dx = dx + 1       
        count = count + 1
    
    return -1


for _ in range(T):
    n, m , x, y  = map(int, input().split())
    result.append(caing(n,m,x,y))

for i in result:
    print(i)    
'''    


