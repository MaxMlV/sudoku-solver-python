board = [
    [0, 0, 7, 9, 0, 6, 0, 0, 0],
    [3, 0, 0, 0, 7, 0, 6, 4, 0],
    [8, 6, 0, 0, 0, 0, 0, 7, 9],
    [1, 0, 0, 0, 0, 9, 0, 3, 0],
    [0, 0, 0, 0, 2, 3, 9, 1, 0],
    [2, 0, 9, 0, 6, 0, 0, 8, 0],
    [0, 7, 4, 3, 9, 0, 0, 0, 8],
    [9, 0, 1, 8, 0, 7, 0, 6, 3],
    [0, 0, 3, 6, 0, 0, 0, 9, 7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

print_board(board)