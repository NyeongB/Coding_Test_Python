'''
출제 : 백준
난이도 : 실버 1
문제 : 숨바꼭질
날짜 : 21.01.13
유형 : BFS
'''
n, k = map(int,input().split())

queue = []
visited = {}
visited[n] = n 
queue.append([n,0])

while queue :
    temp = queue.pop(0)
    x = temp[0]
    if x == k:
        print(temp[1])
        break
    
    if visited.get(x-1,-1) == -1 and (0<=x-1):
        queue.append([x-1,temp[1]+1])
        visited[x-1] = x-1
    
    if visited.get(x+1,-1) == -1 and (x+1<=100000):
        queue.append([x+1,temp[1]+1])
        visited[x+1] = x+1

    if visited.get(x*2,-1) == -1 and (x*2<=100000):
        queue.append([x*2,temp[1]+1])
        visited[x*2] = x*2

'''
딕셔너리로 방문체크를 했는데
파이썬에서 이방법이 좋은지 체크해봐야한다.

'''