'''
출제 : 프로그래머스
난이도 : 레벨 1
문제 : K번째 수
날짜 : 21.01.05
유형 : 정렬
'''

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for command in commands :
        i, j, k = command[0], command[1], command[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer

answer = solution(array, commands)

for i in answer:
    print(i,end=" ")

'''
파이썬 전향 후 첫 문제
파이썬이 아직 너무 익숙치 않음
'''