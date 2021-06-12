'''
출제 : 프로그래머그
난이도 : 레벨 2
문제 : 네트워크
날짜 : 21.06.12
유형 : DFS
'''
def dfs(n,i,visited,computers):
    visited.add(i)
    for j in range(n):
        if i != j and j not in visited and computers[i][j] == 1:
            dfs(n,j,visited,computers)

def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            answer += 1
            dfs(n,i,visited,computers)
    return answer

'''
기본적인 dfs 문제 감을 익혀야겠다
'''    