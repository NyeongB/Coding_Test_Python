'''
출제 : 백준
난이도 : 실버 3
문제 : 에디터
날짜 : 21.04.06
유형 : 스택
'''

lStack = list(map(str, input()))
rStack = []


n = int(input())

for _ in range(n):
    c = input().split()
    if c[0] == 'L' and lStack != []:
        rStack.append(lStack.pop())
    elif c[0] == 'D' and rStack != []:
        lStack.append(rStack.pop())
    elif c[0] == 'B' and lStack != []:
        lStack.pop()
    elif c[0] == 'P':
        lStack.append(c[1])

for i in lStack:
    print(i,end='')
while rStack:
    print(rStack.pop(),end='')
    


'''
예전에 풀어본 문제인데 구조가 잘 이해안되서 좀 생각하고 풀었다.
'''