'''
출제 : 백준
난이도 : 골드 5
문제 : 치킨 배달
날짜 : 21.04.20
유형 : 브루트포스
'''
from itertools import combinations

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

chikens = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chikens.append((i, j))

combi = list(combinations(chikens,m))
#print(combi)
result = []
for c in range(len(combi)):
    sum = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                Min = 1e9
                for k in combi[c]:
                    Min = min(Min, int(abs(i-k[0]))+int(abs(j-k[1])))
                sum += Min
    result.append(sum)
result.sort()
print(result[0])

'''
itertools 의 combinations 를 이용해 치킨 가게의 조합을 먼저 구하고 시작했다.
핵심은 i,j가 1일때 해당 조합의 최소를 구하고 sum으로 더해놓은다음 리스트에 쌓은다음 제일 낮은 값을 출력하면 된다.
'''