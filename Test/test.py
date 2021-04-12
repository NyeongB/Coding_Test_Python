arr = [[0,0,0], [0,0,0], [0,0,0]]

print(arr)
c = 0

def p():
    l = len(arr)
    for i in range(l):
        for j in range(l):
            print(arr[i][j],end=' ')
        print()


def dfs(count):
    global c
    if c > 30:
        return
    if count == 3:
        c +=1
        p()
        print()
        return
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(count + 1)
                arr[i][j] = 0


dfs(0)