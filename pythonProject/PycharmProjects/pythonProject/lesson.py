board = []

for i in range(5):
    board.append(input())


def row():
    count_row = 0
    result = "D"
    for i in range(5):
        for j in range(5):
            pivot = board[i][0]
            if board[i][j] == pivot and pivot != ".":
                count_row += 1
        if count_row == 5:
            result = pivot
            return result
        count_row = 0
    return result


def line():
    result = "D"
    count_line = 0
    for i in range(5):
        for j in range(5):
            pivot = board[0][i]
            if board[j][i] == pivot and pivot != ".":
                count_line += 1
        if count_line == 5:
            result = pivot
            return result
        count_line = 0
    return result


def cross():
    result = "D"
    pivot = board[0][0]
    pivot2 = board[0][4]
    count_cross = 0
    count_cross2 = 0

    for i in range(5):
        for j in range(5):
            if i == j and pivot == board[i][j]:
                count_cross += 1

            if i + j == 4 and pivot2 == board[i][j]:
                count_cross2 += 1

    if count_cross == 5:
        result = pivot
        return result
    elif count_cross2 == 5:
        result = pivot2
        return result
    count_cross = 0
    count_cross2 = 0
    return result

#print(row(),line() ,cross())
if row() != 'D':
    print(row())
elif line() != 'D':
    print(line())
elif cross() != 'D':
    print(cross())
else:
    print('D')
