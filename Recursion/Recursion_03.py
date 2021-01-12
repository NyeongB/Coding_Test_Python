'''
출제 : 백준
난이도 : 실버 2
문제 : 로또
날짜 : 21.01.12
유형 : 재귀
'''

def combi(index, depth) :
    if depth == 6 :
        for i in range(n):
            if select[i] :
                print(arr[i], end=" ")
        print()
        return
    
    for i in range(index, n):
        if select[i] == 0 :
            select[i] = 1
            combi(i+1, depth+1)
            select[i] = 0

while True :
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break
    n = input_data[0]
    arr = input_data[1:]
    select = [0] * n
    combi(0, 0) # index, depth
    print()


