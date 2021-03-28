'''
출제 : 백준
난이도 : 실버 5
문제 : 캠핑
날짜 : 21.03.28
유형 : 그리디
'''

result = []

while True : 
    l, p, v = map(int, input().split())
    if l ==0 and p ==0 and v == 0:
        break
    
    t = (v // p) * l
    r = v % p
    if r >= l:
        t = t + l
    else :
        t = t + r
    result.append(t)

for i, v in enumerate(result):
    print("Case "+str(i+1)+": "+ str(v))


'''
핵심은 나머지 다루는거 
나머지라고 전체를 다 넣으면 안된다.
'''