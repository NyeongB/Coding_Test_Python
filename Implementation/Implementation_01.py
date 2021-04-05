'''
출제 : 백준
난이도 : 실버 4
문제 : 사탕게임
날짜 : 21.04.05
유형 : 구현
'''

def return_max(graph):
    n = len(graph)
    result = 0
    for i in range(n):
        row = 1
        col = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                row += 1
            else :
                result = max(result, row)
                row = 1

        
            if graph[j][i] == graph[j+1][i]:
                col += 1
            else :
                result = max(result, col)
                col = 1
        result = max(result, row, col)
    
    return result

n = int(input())

graph = list( list(map(str,input())) for _ in range(n))

answer = 0

for i in range(n):
    for j in range(n-1):
        if graph[i][j] != graph[i][j+1]:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j] #돌리기 작업
            answer = max(answer, return_max(graph))
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j] #체크 후 원래데로 돌리기

        if graph[j][i] != graph[j+1][i]:
            graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

            answer = max(answer, return_max(graph))
            graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

print(answer)

'''
실버4인데 생각보다 쉽지않음 
또 풀어봐야겠다 
'''