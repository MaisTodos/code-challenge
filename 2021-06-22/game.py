def run_turn(cells):
    response = []
    for x, y in cells:
        count = 0
        if (x-1, y) in cells:
            count += 1
        if (x+1, y) in cells:
            count += 1
        if (x, y-1) in cells:
            count += 1
        if (x, y+1) in cells:
            count += 1
        if (x-1, y-1) in cells:
            count += 1
        if (x+1, y+1) in cells:
            count += 1

        if count < 2 or count > 3:
            "MORRE DESGRACADO!"
        if count = 2 or count

vizinhanca = [(0, 1), (1, 0), (1, 1), (0, 1), (1, 1), (1, 2), (2, 1), (1, 1), (1, 2)]



if __name__ == "__main__":
    cells = [(0, 0), (0, 2), (2, 2)]

    turn = run_turn(cells)
    assert turn == [(0, 1), (0, 2)]



# board = [
#     [Cell(0, 0), Cell(0, 1), Cell(0, 2)],
#     [Cell(1, 0), Cell(1, 1), Cell(1, 2)],
#     [Cell(2, 0), Cell(2, 1), Cell(2, 2)],
# ]