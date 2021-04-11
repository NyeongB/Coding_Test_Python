'''
출제 : 백준
난이도 : 실버 4
문제 : 제로
날짜 : 21.04.11
유형 : 스택
'''

n = int(input())
stack = list()
for _ in range(n):
    temp = int(input())
    if len(stack) !=0 and temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))

'''
눈감고 풀었다.
'''