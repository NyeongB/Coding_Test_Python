n = int(input())

map = [list(map(int,input().split())) for _ in range(n)]

queue = []

def bfs():
    queue = [(0,0,0)]   # r,c,방향 
    count = 0
    while queue:
        temp = queue.pop(0)
        x = temp[0]
        y = temp[1]
        d = temp[2]

        if d == 0:
            dx = x + 0
            dy = y + 1
            
            if map[dx][dy] == 0:
                if dx == n-1 and dy== n-1:
                    count +=1
                else :
                    if dy+1<n:
                        if map[dx][dy+1] == 0:
                            queue.append([dx,dy,0])
                    if dy+1<n and dx+1<n:
                        if map[dx+1][dy] ==0 and map[dx][dy+1] == 0 and map[dx+1][dy+1] ==0:
                            queue.append([dx,dy,2])
                
        elif d == 1:
            dx = x + 1
            dy = y + 0
            
            if map[dx][dy] == 0:
                if dx == n-1 and dy== n-1:
                    count +=1
                else :
                    if dx+1<n:
                        if map[dx+1][dy] == 0:
                            queue.append([dx,dy,1])
                    if dy+1<n and dx+1<n:
                        if map[dx+1][dy] ==0 and map[dx][dy+1] == 0 and map[dx+1][dy+1] ==0:
                            queue.append([dx,dy,2])
        elif d == 2:
            dx = x + 1
            dy = y + 1
            
            if map[dx][dy] == 0:
                if dx == n-1 and dy== n-1:
                    count +=1
                else :
                    if dy+1<n:
                        if map[dx][dy+1] == 0:
                            queue.append([dx,dy,0])
                    if dx+1<n:
                        if map[dx+1][dy] == 0:
                            queue.append([dx,dy,1])
                    if dy+1<n and dx+1<n:
                        if map[dx+1][dy] ==0 and map[dx][dy+1] == 0 and map[dx+1][dy+1] ==0:
                            queue.append([dx,dy,2])

    return count

print(bfs())
    
