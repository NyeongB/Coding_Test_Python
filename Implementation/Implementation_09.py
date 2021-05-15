'''
출제 : 백준
난이도 : 골드 5
문제 : 틱택토
날짜 : 21.05.15
유형 : 구현
'''

def tictacto(string):
    
    count_X, count_O = string.count('X'), string.count('O')
    if count_X - count_O != 1 and count_X - count_O != 0: return 'invalid'
    
    
    board = [[''] * 3 for _ in range(3) ]

    for i in range(9):
        board[i//3][i%3] = string[i]

    bingo_X, bingo_O = 0, 0

    # 가로
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] =='X':
                bingo_X += 1
            elif board[i][0] =='O':
                bingo_O += 1
    # 세로
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] =='X':
                bingo_X += 1
            elif board[0][i] =='O':
                bingo_O += 1
    # 대각선
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] =='X':
            bingo_X += 1
        elif board[0][0] =='O':
            bingo_O += 1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] =='X':
            bingo_X += 1
        elif board[0][2] =='O':
            bingo_O += 1


    if count_X - count_O == 1:
        if bingo_O: return 'invalid'

    elif count_X == count_O:
        if bingo_X: return 'invalid'


    if count_O + count_X != 9 and (not bingo_X and not bingo_O): return 'invalid'
    
    return 'valid'

result = []

while True:
    INPUT = str(input())
    if INPUT == 'end':
        break
    result.append(tictacto(INPUT))

for i in result:
    print(i)