'''
출제 : 프로그래머스
난이도 : 레벨 3
문제 : 네트워크
날짜 : 21.04.11
유형 : DFS
'''
def dfs(v, visited,c):
    visited[v] = 1
    for i in range(len(c)):
        if visited[i] == 0 and c[v][i] == 1 and v != i:
            dfs(i,visited,c)
    
    
def solution(n, computers):
    answer = 0
    c = computers
    visited = [0] * n 
    for i in range(n):
        if visited[i] == 0:
            dfs(i,visited, c)
            answer += 1
    
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


'''
'''