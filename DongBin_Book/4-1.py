# 21.01.11
# p.110
n = int(input())
plans = input().split()
x = 1
y = 1
# R L D U
dx =[0,0,1,-1]
dy =[1,-1,0,0]

move = ["R", "L", "D", "U"]


for temp in plans:
  i = move.index(temp)
  nx = x + dx[i]
  ny = y + dy[i]

  if nx<1 or ny<1 or ny>n or nx >n:
    continue
  x, y = nx, ny

print(nx,ny)