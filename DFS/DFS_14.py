'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 타겟 넘버
날짜 : 21.05.28
유형 : DFS
'''

answer = 0
def solution(numbers, target):
    
    dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, index, total):
    global answer
    if len(numbers) == index:
        if target == total:
            answer += 1
        return
    
    dfs(numbers, target, index + 1, total + numbers[index])
    dfs(numbers, target, index + 1, total + numbers[index] * -1)