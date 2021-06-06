'''
출제 : 프로그래머스
난이도 : 레벨 3
문제 : 입국 심사
날짜 : 21.06.06
유형 : 이분 탐색
'''
def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    
    while start <= end:
        mid = (start+end) // 2
        
        total = 0
        
        for i in times:
            total += mid // i
            if total >= n:
                break
        
        if total >= n:
            answer = mid
            end = mid - 1
        elif total < n:
            start = mid + 1
        
    return answer


'''
문제를 외운다.
'''