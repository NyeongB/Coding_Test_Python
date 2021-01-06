'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 타깃넘버
날짜 : 21.01.05
유형 : DFS
'''
answer = 0  #전역변수
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, index, total) :
    global answer   #전역변수 컨트롤 가능
    if len(numbers) == index:
        if total == target :
            answer += 1
        return
    
    dfs(numbers, target, index+1, total + numbers[index])
    dfs(numbers, target, index+1, total + numbers[index]*-1)

# 테스트
print(solution([1,1,1,1,1],3))

'''
파이썬은 들여쓰기가 굉장히 중요하다
아직 가로가없는게 불편하고 잘 안보이긴한다.
문제의 핵심은 모든 케이스를 다 더했을떄 타깃넘버냐 아니냐이고 
인덱스와 두개의 +,- 재귀가 중요하다.
'''