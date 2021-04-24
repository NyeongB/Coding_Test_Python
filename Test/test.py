# 방향 조정
d_flag = [] 
d_flag.append(2)
d_flag.append(2)
d_flag.append(0)
d_flag.append(6)


flag = 0
odd, even = 0,0
print(d_flag)
for i, v in enumerate(d_flag):
    if i ==0:
        if v % 2 ==0:
            even = 1
        else:
            odd = 1
    else:
        if odd == 1 and v % 2 == 0:
            flag = 1
        elif even == 1 and v% 2 !=0:
            flag = 1
print(flag)