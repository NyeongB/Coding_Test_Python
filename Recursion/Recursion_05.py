'''
출제 : 백준
난이도 : 골드 5
문제 : 압축
날짜 : 21.03.29
유형 : 재귀
'''
visit = list([True] * 51)

s = input()

def dfs(s, index):
    cnt = 0
    for i in range(index, len(s)):
        t = s[i]
        if t =='(' and visit[i] :
            visit[i] = False
            cnt = cnt - 1
            cnt = cnt + int(s[i-1]) * dfs(s, i + 1)
            
        elif t ==')' and visit[i]:
            visit[i] = False
            return cnt
        elif visit[i]:
            visit[i] = False
            cnt = cnt + 1
    return cnt
print(dfs(s,0))