# 21.01.11
# p.115

input_data = input()
count = 0

x = int(input_data[1])
y = ord(input_data[0]) - 97 + 1

# 나이트가 움직일 수 있는 8 방향 
dx = [-2,-2,-1,1,2,2,-1,1]
dy = [-1,1,2,2,-1,1,-2,-2]

for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx>0 and ny >0 and nx<=8 and ny <=8:
    count += 1

print(count)

'''
동빈나는 리스트에 8방향 튜플넣고 리스트 자체를 포문 돌림 
'''