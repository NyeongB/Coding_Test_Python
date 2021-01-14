'''
출제 : 백준
난이도 : 실버 3
문제 : N과 M(3)
날짜 : 21.01.14
유형 : Backtracking
'''
n, m = map(int, input().split())
output = []
def dfs(depth,index):
    if depth == m :
        print(' '.join(output))
        return
    
    for i in range(index, n+1):
        output.append(str(i))
        dfs(depth + 1,i)
        output.pop()

dfs(0,1)