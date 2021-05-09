'''
출제 : 백준
난이도 : 실버 3
문제 : 1,2,3 더하기
날짜 : 21.05.09
유형 : 재귀
'''

def recursion(target, sum):
    if target == sum:
        return 1
    elif target < sum:
        return 0
    
    result = 0
    for i in range(1, 4):
        result += recursion(target, sum + i)

    
    return result

n = int(input())

result = []

for _ in range(n):
    target = int(input())
    result.append(recursion(target, 0))

for i in result:
    print(i)

'''
예전에 풀었던 문제지만 좋은 문제
'''