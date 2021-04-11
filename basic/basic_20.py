'''
출제 : 백준
난이도 : 실버 5
문제 : 날짜 계산
날짜 : 21.04.11
유형 : 수학
'''
e, s, m = map(int, input().split())

y = 1

while True:
    if (y-e)%15 == 0 and (y-s)%28 ==0 and (y-m)%19 ==0:
        break
    y+=1

print(y)


'''
외워야함 백준 강의 보는걸로 
'''

