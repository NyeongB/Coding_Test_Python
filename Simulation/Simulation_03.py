'''
출제 : 백준
난이도 : 골드 5
문제 : 미세먼지 안녕!
날짜 : 21.04.15
유형 : 시뮬레이션
'''
import sys

d = [(-1,0),(0,1),(1,0),(0,-1)]
d2 = [(1,0),(0,1),(-1,0),(0,-1)]

def spread(x, y):
    count = 0
    value = int(arr[x][y]/5)
    for i in range(4):
        dx = x + d[i][0]
        dy = y + d[i][1]
        if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] != -1:
            count += 1
            temp[dx][dy] += value
    temp[x][y] += arr[x][y]
    temp[x][y] -= value * count

if __name__ == '__main__':

    r, c, t = map(int, sys.stdin.readline().rstrip().split())

    arr = []
    answer = 0
    air = []

    for _ in range(r):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for _ in range(t):
        # t 만큼 반복 
        
        # 1. 확산 
        # 1) 빈 배열 만들기
        temp = list(list([0]*c) for _ in range(r))
        # 2)확산
        for i in range(r):
            for j in range(c):
                if arr[i][j] > 4:
                    spread(i,j)
                else:
                    temp[i][j] += arr[i][j]
                if arr[i][j] == -1:
                    air.append((i,j))
        # 3)복사
        arr = temp

        # 2. 청정기 가동
        # 1) 위 청정기 가동
        index = 0
        a_x, a_y = air.pop(0)
        s_x, s_y = (0,0)
        l_x, l_y = (a_x, c-1)
        while index <4:
            dx = a_x + d[index][0]
            dy = a_y + d[index][1]
            if s_x <= dx <= l_x and s_y <= dy <= l_y:
                if arr[a_x][a_y] != -1 :
                    if arr[dx][dy] != -1:
                        arr[a_x][a_y] = arr[dx][dy]
                    else:
                        arr[a_x][a_y] = 0
                
                a_x, a_y = (dx, dy)
            else :
                index +=1

        # 2) 아래 청정기 가동
        index = 0
        a_x, a_y = air.pop(0)
        s_x, s_y = (a_x, a_y)
        l_x, l_y = (r-1, c-1)
        while index <4:
            dx = a_x + d2[index][0]
            dy = a_y + d2[index][1]
            if s_x <= dx <= l_x and s_y <= dy <= l_y:
                if arr[a_x][a_y] != -1 :
                    if arr[dx][dy] != -1:
                        arr[a_x][a_y] = arr[dx][dy]
                    else:
                        arr[a_x][a_y] = 0
                
                a_x, a_y = (dx, dy)
            else :
                index +=1




    '''
    # 3. 반복문 끝나면 체크
    for i in range(r):
        for j in range(c):
            print(arr[i][j],end=' ')
        print()
    '''
    
    for i in arr:
        answer += sum(i)
    print(answer+2)


'''
구현 한시간 걸림
한번에 성공해서 기쁨..!
핵심은 확산은 쉬운데
공기 청정기 방향을 잘 선정해서 두분야로 나눠서함
레퍼런스 한번 참고해야겠다(더 쉽게 풀었을것같음..)
'''