import random


def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0
    PrintGrid(Grid)


def PrintGrid(Grid):

    TableTB = "|--------------------------------|"
    TableMD = "|----------|----------|----------|"

    print(TableTB)

    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y == 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if y == 8:
                print("|")
    print(TableTB)


MakeSudoku()

# |-----------------------|
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# |-------|-------|-------|
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# |-------|-------|-------|
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# |-----------------------|
