dx = [1,0,-1,0] # 남 동 북 서 
dy = [0,1,0,-1]

def rotate(x1,y1,x2,y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    idx = 0
    x = x1
    y = y1
    Min = 1e9
    temp = arr[x][y]
    while idx < 4:
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if x1 <= nx <= x1 and y1 <= ny <= y2:
            arr[x][y] = arr[nx][ny]
            x = nx
            y = ny
        else:
            idx +=1
            
    for i in arr:
        print(' '.join(map(str,i)),end='\n')
        
    return Min
    


def solution(rows, columns, queries):
    answer = []
    
    arr = list( ([0]*columns) for _ in range(rows))
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    
    for x1,y1,x2,y2 in queries:
        rotate(x1,y1,x2,y2)
    
    
    
    return answer