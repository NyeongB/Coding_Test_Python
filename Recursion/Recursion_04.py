'''
출제 : 백준
난이도 : 실버 3
문제 : N과 M (1)
날짜 : 21.01.12
유형 : 재귀, 순열
'''

def permutation(depth) :
    if depth == p:
        for i in range(p):
            print(output[i], end=" ")
        print()

    for i in range(n) :
        if visited[i] == False:
            visited[i] = True
            output[depth] = i + 1
            permutation(depth + 1)
            visited[i] = False
            


n, p = map(int, input().split())
output = [0] * n
visited = [False] * n
permutation(0)

