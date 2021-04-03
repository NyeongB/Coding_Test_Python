'''
출제 : 백준
난이도 : 실버 5
문제 : 방 번호
날짜 : 21.04.03
유형 : 구현
'''
import math

n = list(map(int,input()))

arr = list([0] * 9)


for i in n:
    if i == 6 or i == 9:
        arr[5] += 0.5
    else :
        arr[i] += 1



print( math.ceil(max(arr)) )



'''
'''