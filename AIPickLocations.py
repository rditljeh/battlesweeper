import random

def AI_pick_mines(Board, totalMines):
    AIlocations = []
    for i in range(totalMines):
        randomCellx = random.randint(0, Board.width - 1)
        randomCelly = random.randint(0, Board.height - 1)
        #AI_adds_mines(Board, randomCellx, randomCelly)
        Board.AIplaced.append([randomCellx, randomCelly])
        AIlocations.append([randomCellx, randomCelly])
    return AIlocations





#could be done in main later
def AI_adds_mines(Board, x, y):
    Board.addMine(x, y)