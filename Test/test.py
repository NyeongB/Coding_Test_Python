from collections import deque


arr = [1,1,1,1,1,9,1]

q = deque((v,i) for i, v in enumerate(arr))
#q = deque((i,v) for i, v in enumerate(arr))

print(max(q))

#좀 충격인게 v,i 로 뽑아야지 맥스 가능하고 i, v로 고대로 뽑으면 밸류 부분에서 max()가 안됌