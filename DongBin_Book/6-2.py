# 21.01.20
# p.181
# 성적이 낮은 순서로 학생 출력하기

n = int(input())


array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda x:x[1])

for i in array:
    print(i[0], end=' ')