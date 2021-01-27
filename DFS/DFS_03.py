'''
출제 : 프로그래머스
난이도 : 레벨 3
문제 : 섬 연결하기
날짜 : 21.01.27
유형 : DFS
'''

def solution(n, costs):

    answer = 0

    graph = [[0] * n for _ in range(n)]

    for i in costs:
        a = i[0]
        b = i[1]
        c = i[2]
        graph[a][b] = graph[b][a] = c
    
    visited = {0:0} # 0 번 방문

    # 함수 시작
    def prim(total, count):
        if n == count:
            return total
        
        min = 9999
        min_index = -1
        for i in range(n):
            if i in visited:
                for j in range(n):
                    if graph[i][j] > 0 and not j in visited:
                        if min > graph[i][j]:
                            min = graph[i][j]
                            min_index = j

        count += 1
        total += min
        visited[min_index] = min_index

        return prim(total, count)

    # 함수 끝
    answer = prim(0,1)
    return answer




print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

'''
테스트용으로 def 안에 def로 구현해봤는데 다음에는 
밖으로 빼서 사용해봐야겠다.. (귀찮아서 이렇게함)
핵심은 0에서 갈수있는거 체크후 
방문한곳으로 부터 뻗어 나가야한다
그뒤로는 방문했던곳중에서 비용이 가장 낮은 것을 선택하는게 핵심
'''