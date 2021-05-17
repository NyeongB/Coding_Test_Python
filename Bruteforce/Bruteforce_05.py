'''
출제 : 백준
난이도 : 실버 5
문제 : 수 이어가기
날짜 : 21.05.17
유형 : 브루트포스
'''

n = int(input())

answer_arr = []
answer = -1

for i in range(1,n+1):
    arr = [n,i]
    temp1 = n
    temp2 = i
    temp3 = n - i
    while temp3 >= 0:
        arr.append(temp3)
        temp1 = temp2
        temp2 = temp3
        temp3 = temp1 - temp2
    
    if answer < len(arr):
        answer = len(arr)
        answer_arr = arr

print(answer)
print(*answer_arr)

'''
당연히 시작점은 절반이상으로 해야되는줄 알았는데
계속 틀려서 
1로 시작점을 잡으니깐 해결되네
'''