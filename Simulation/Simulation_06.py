'''
출제 : 백준
난이도 : 실버 5
문제 : 나무 조각
날짜 : 21.05.05
유형 : 시뮬레이션
'''

arr = list(map(int, input().split()))



while arr != [1,2,3,4,5]:
    flag = True
    for i in range(4):
        if arr[i] > arr[i+1]:
            # 둘의 위치를 바꾸고
            arr[i], arr[i+1] = arr[i+1], arr[i]
            #print(' '.join(map(str,arr)))
            print(*arr)

'''
문제 조건 제대로 안보고 방심하다 처음에 틀렸다

파이썬 대단한게 레퍼런스 변수랑 != [1,2,3]
이렇게 조건식잡으면 하나씩 비교해서 결과 알려주나보다

'''