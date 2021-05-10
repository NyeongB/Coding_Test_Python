'''
출제 : 프그
난이도 : 레벨 2
문제 : 행렬 테두리 회전하기
날짜 : 21.05.10
유형 : 구현
'''
dx = [1,0,-1,0] # 남 동 북 서 
dy = [0,1,0,-1]


def solution(rows, columns, queries):
    
    def rotate(x1,y1,x2,y2):
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        idx = 0
        x = x1
        y = y1
        
        temp = arr[x][y]
        Min = temp
        while idx < 4:
            nx = x + dx[idx]
            ny = y + dy[idx]

            if x1 <= nx <= x2 and y1 <= ny <= y2:
                Min = min(Min,arr[nx][ny])
                arr[x][y] = arr[nx][ny]
                x = nx
                y = ny
            else:
                idx +=1
        arr[x1][y1+1] = temp
        
       

        return Min
    
    
    answer = []
    
    arr = list( ([0]*columns) for _ in range(rows))
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(x1,y1,x2,y2))
    
    
    
    return answer