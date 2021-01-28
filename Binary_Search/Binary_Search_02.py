'''
출제 : 프로그래머스
난이도 : 레벨 3
문제 : 입국심사
날짜 : 21.01.28
유형 : 이분 탐색
'''
def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    while start <= end:
        mid = (start+end)//2
        
        total = 0
        for i in times:
            total += mid//i
            if total >= n:
                break
        
        if total >=n:
            answer = mid
            end = mid - 1
        elif total < n :
            start = mid + 1


        
    return answer

print(solution(6,[7,10]))
'''
for문을 돌때 중간 중간 total을 확인해서 n보다 크면 바로 break 처리해야 시간 초과가 안난다.
'''