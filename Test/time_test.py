from random import randint
import time


# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1,100))

# 선택 정렬 프로그램 선능 츠정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑

end_time = time.time()
print("선택 정렬 선능 측정 :",end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1,100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정 :", end_time-start_time)

'''
선택 정렬 선능 측정: 6.054190635681152
기본 정렬 라이브러리 성능 측정: 0.0010371208190917969
'''