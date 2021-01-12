'''
출제 : 백준
난이도 : 실버 2
문제 : 나이트의 이동
날짜 : 21.01.13
유형 : BFS
'''

t = int(input())
n = 0
start = []
end = []
dx = [-2,-2,-1,1,2,2,-1,1]
dy = [-1,1,2,2,-1,1,-2,-2]
visited = []
for _ in range(t):
    n = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    visited = [([False] * n ) for _ in range(n)]
    queue = [(start[0],start[1],0)]
    count = 0
    flag = False
    if start[0] == end[0] and start[1] == end[1]:
        flag = True
        print(0)
    while queue :
        if flag :
            break
        temp = queue.pop(0)

        for i in range(8):
            nx = dx[i] + temp[0]
            ny = dy[i] + temp[1]
            count = temp[2] + 1
            if nx == end[0] and ny == end[1]:
                flag = True
                print(count)
                break
            if nx >= 0 and ny >=0 and nx <n and ny < n:
                if visited[nx][ny] :
                    continue
                visited[nx][ny] = True
                queue.append((nx,ny,count))


'''
dfs로 풀었으면 아마 시간이 엄청 오바됐을거다
핵심은 갔던곳 다시 방문 못하게 하는거랑
bfs 돌면서 다음 칸을 이동할때마다 +1한 count를 함께 이동방향과 큐에 넣어주면서 달고 다녀야한다.
0,0 이면 바로 출력해버리고..
'''
                
    

    


