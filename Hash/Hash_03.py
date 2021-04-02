'''
출제 : 백준
난이도 : 실버 4
문제 : 비밀번호 찾기
날짜 : 21.04.02
유형 : 해시
'''

n, m = map(int, input().split())

d = {}

for _ in range(n):
    key, value = map(str, input().split())
    d[key] = value

result = []

for _ in range(m):
    key = input()
    result.append(d[key])

for i in result:
    print(i)

'''
딕셔너리에 익숙해지자
'''