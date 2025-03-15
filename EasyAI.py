import random


def AI_move_randomly(Board):
    selections = checks_all_possible_selections(Board)
    print("selections", selections)
    AIPlacedBombs = Board.AIplaced#checkKnown(Board)
    for i in AIPlacedBombs:
        if i in selections:
            selections.remove(i)
    randomCell = random.randint(0, len(selections) - 1)
    w, v = selections[randomCell]
    #w=x, y=v
    return w, v

def checks_all_possible_selections(Board):
    canBeSelected = []
    for i in range(0, Board.width):
        for j in range(0, Board.height):
            if not Board.cell_dict[f"{i},{j}"]["selected"]:#
                canBeSelected.append([i, j])
    return canBeSelected