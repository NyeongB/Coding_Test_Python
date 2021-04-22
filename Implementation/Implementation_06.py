'''
출제 : 백준
난이도 : 골드 3
문제 : 경사로
날짜 : 21.04.22
유형 : 구현
'''

n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
# 가로 검사
for i in range(n):
    pre = arr[i][0]
    cnt = 1
    for j in range(1,n):
        
        if pre == arr[i][j]:
            cnt += 1
            pre = arr[i][j]
        elif pre + 1 == arr[i][j] and cnt >= 0:
            if cnt >= l:
                cnt = 1
                pre = arr[i][j]
            else:
                break
        elif pre - 1 == arr[i][j] and cnt >= 0:
            cnt = -l + 1
            pre = arr[i][j]
        else:
            break
    else :
        if cnt >= 0:
            ans += 1



# 세로 검사
for j in range(n):
    pre = arr[0][j]
    cnt = 1
    for i in range(1,n):
        if arr[i][j] == pre:
            cnt += 1
            pre = arr[i][j]
        elif arr[i][j] == pre+1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                pre = arr[i][j]
            else:
                break
        elif arr[i][j] == pre-1 and cnt >= 0:
            cnt = - l + 1
            pre = arr[i][j]
        else:
            break
    else:
        if cnt >= 0:
            ans += 1

print(ans)

'''
cnt를 이용하여 오를수있는 경사 기반을 검사하고 
내려갔을때 cnt가 음수값이 되지않는것을 판단해 ans 카운트를 고려한다
핵심은 pre로 잡아놓은 전의 값을 계속 비교하는것
레퍼런스를 보고 풀었다
'''