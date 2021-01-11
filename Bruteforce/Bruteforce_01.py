'''
출제 : 백준
난이도 : 실버 3
문제 : 스타트와 링크
날짜 : 21.01.11
유형 : 브루트포스
'''
from itertools import combinations

def tema_sum(team, S) :
    num = len(team)
    sumv = 0
    for x in range(0, num-1):
        for y in range(x+1, num):
            sumv = sumv + S[team[x]][team[y]] + S[team[y]][team[x]]
    return sumv

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

team = list(combinations(range(N), N//2 ))
start_team = []
link_team = []

for _ in range(len(team)//2):
    start_team.append(list(team.pop(0)))
    link_team.append(list(team.pop()))

min = 1000000

for i in range(len(start_team)):
    sum = abs(tema_sum(start_team[i],S) - tema_sum(link_team[i],S))
    if min > sum :
        min = sum

print(min)

'''

'''