'''
출제 : 백준
난이도 : 실버 5
문제 : 배열 합치기
날짜 : 21.05.19
유형 : 정렬
'''
a,b = map(int,input().split())

arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))
result = []
i_a = 0
i_b = 0

for _ in range(a+b):

    if i_a == a:
        result.append(arr_b[i_b])
        i_b += 1
        continue
    elif i_b == b:
        result.append(arr_a[i_a])
        i_a += 1
        continue
    

    if arr_a[i_a] > arr_b[i_b]:
        result.append(arr_b[i_b])
        i_b += 1
    else:
        result.append(arr_a[i_a])
        i_a += 1

print(*result)


'''

'''