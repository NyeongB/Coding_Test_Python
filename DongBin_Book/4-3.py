'''
문제 : 왕실의 나이트
날짜 : 21.03.24
유형 : 
'''

s = input()

count = 0

r = int(s[1])
c = int(ord(s[0])) - int(ord('a')) + 1

d = [(2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (1,-2), (-1,-2) ]

for i in d:
    #print(i[0])
    nx = r + i[0]
    ny = c + i[1]
    if 1<= nx <= 8 and 1 <= ny <= 8:
        count = count + 1

print(count)

'''
오타 조심
'''