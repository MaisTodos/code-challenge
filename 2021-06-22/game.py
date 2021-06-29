def run_turn(cells):
    next_turn_cells = []
    neighborhood = []
    for x, y in cells:
        count = 0
        neighborhood.append((x-1, y))
        neighborhood.append((x+1, y))
        neighborhood.append((x, y-1))
        neighborhood.append((x, y+1))
        neighborhood.append((x-1, y-1))
        neighborhood.append((x-1, y+1))
        neighborhood.append((x+1, y+1))
        neighborhood.append((x+1, y-1))
        if (x-1, y) in cells: # a esquerda
            count += 1
        if (x+1, y) in cells: # a direita
            count += 1
        if (x, y-1) in cells: # abaixo
            count += 1
        if (x, y+1) in cells: # acima
            count += 1
        if (x-1, y-1) in cells: # baixa esquerda
            count += 1
        if (x-1, y+1) in cells: # cima esquerda
            count += 1
        if (x+1, y+1) in cells: # cima direita
            count += 1
        if (x+1, y-1) in cells: # baixa direita
            count += 1

        if count < 2 or count > 3:
            pass
        if count == 3 or count == 2:
            next_turn_cells.append((x, y))

    slots = set(neighborhood)
    for slot in slots:
        if neighborhood.count(slot) == 3 and slot not in next_turn_cells:
            next_turn_cells.append(slot)

    return sorted(next_turn_cells)

if __name__ == "__main__":
    assert run_turn([(0, 0), (0, 2), (2, 2)]) == [(1, 1)]
    assert run_turn([(1, 1)]) == []
    assert run_turn([(0, 1), (1, 0), (1, 1), (1, 2)]) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1)]
    assert run_turn([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1)]) == [(-1, 1), (0, 0), (0, 2), (2, 0), (2, 1), (2, 2)]

    result = [(0, 1), (1, 1), (1, 2), (2, 1), (2, 2), (3, 2)]
    for turn in range(10):
        result = run_turn(result)
        print(f"Turno: {turn+1} = {result}")
