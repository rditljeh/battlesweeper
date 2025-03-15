from EasyAI import *


def AI_checks_0s(board):
    for x in range(0, board.width):
        for y in range(0, board.height):
            count_certain_bomb = 0

            if board.cell_dict[f"{x},{y}"]["selected"] and board.cell_dict[f"{x},{y}"]["value"] != 0:
                #print("I got selected: ", i, j)
                #compare surrounding cells

                cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                                  f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]

                for neighbor in cell_neighbors:
                    if neighbor in board.cell_dict.keys():
                        if board.cell_dict[neighbor]["probability"] == 1:
                            count_certain_bomb = count_certain_bomb + 1

                '''
                if (i > 0 and j > 0):
                    if board.board[i-1][j-1].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (j > 0):
                    if board.board[i][j-1].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (i < board.boardSize - 1 and j > 0):
                    if board.board[i+1][j-1].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (i > 0):
                    if board.board[i-1][j].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (i < board.boardSize - 1):
                    if board.board[i+1][j].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (i > 0 and j < board.boardSize - 1):
                    if board.board[i-1][j+1].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (j <board.boardSize - 1):
                    if board.board[i][j+1].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                if (i < board.boardSize - 1 and j < board.boardSize - 1):
                    if board.board[i+1][j+1].probability == 1:
                        #print("in statement")
                        count_certain_bomb = count_certain_bomb + 1
                '''


                #compare cells not selected with this cell's adjacency count
                if count_certain_bomb == board.cell_dict[f"{x},{y}"]["value"]:
                    set_all_certain_safe(board, x, y)
            elif board.cell_dict[f"{x},{y}"]["selected"] and board.cell_dict[f"{x},{y}"]["value"] == 0:
                set_all_certain_safe(board, x, y)

#sets any adjacent cells that are not 100% chance to 0% chance
def set_all_certain_safe(Board, x, y):
    cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                      f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]

    for neighbor in cell_neighbors:
        if neighbor in Board.cell_dict.keys():
            if not Board.cell_dict[neighbor]["selected"] and not Board.cell_dict[neighbor]["probability"] == 1:
                Board.cell_dict[neighbor]["probability"] = 0



    '''
    if (i > 0 and j > 0):
        if Board.board[i - 1][j - 1].selected == False and Board.board[i - 1][j - 1].probability != 1:
            Board.board[i - 1][j - 1].probability = 0
    if (j > 0):
        if Board.board[i][j - 1].selected == False and Board.board[i][j - 1].probability != 1:
            Board.board[i][j - 1].probability = 0
    if (i < Board.boardSize - 1 and j > 0):
        if Board.board[i + 1][j - 1].selected == False and Board.board[i + 1][j - 1].probability != 1:
           Board.board[i + 1][j - 1].probability = 0
    if (i > 0):
        if Board.board[i - 1][j].selected == False and Board.board[i - 1][j].probability != 1:
            Board.board[i - 1][j].probability = 0
    if (i < Board.boardSize - 1):
        if Board.board[i + 1][j].selected == False and Board.board[i + 1][j].probability != 1:
            Board.board[i + 1][j].probability = 0
    if (i > 0 and j < Board.boardSize - 1):
        if Board.board[i - 1][j + 1].selected == False and Board.board[i - 1][j + 1].probability != 1:
            Board.board[i - 1][j + 1].probability = 0
    if (j < Board.boardSize - 1):
        if Board.board[i][j + 1].selected == False and Board.board[i][j + 1].probability != 1:
            Board.board[i][j + 1].probability = 0
    if (i < Board.boardSize - 1 and j < Board.boardSize - 1):
        if Board.board[i + 1][j + 1].selected == False and Board.board[i + 1][j + 1].probability != 1:
            Board.board[i + 1][j + 1].probability = 0
            '''

#for every cell with a nonzero number, if it has been selected, compare its number to adjacent unselected cells. if equal, all adjacent cells are 100% a mine
def AI_checks_100s(board):
    for x in range(0, board.width):
        for y in range(0, board.height):
            count_not_clicked = 0

            if board.cell_dict[f"{x},{y}"]["selected"] and board.cell_dict[f"{x},{y}"]["value"] != 0:

                cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                                  f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]

                for neighbor in cell_neighbors:
                    if neighbor in board.cell_dict.keys():
                        if not board.cell_dict[neighbor]["selected"]:
                            count_not_clicked = count_not_clicked + 1

                '''
                #print("I got selected: ", i, j)
                #compare surrounding cells
                if (i > 0 and j > 0):
                    if board.board[i-1][j-1].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (j > 0):
                    if board.board[i][j-1].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (i < board.boardSize - 1 and j > 0):
                    if board.board[i+1][j-1].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (i > 0):
                    if board.board[i-1][j].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (i < board.boardSize - 1):
                    if board.board[i+1][j].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (i > 0 and j < board.boardSize - 1):
                    if board.board[i-1][j+1].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (j <board.boardSize - 1):
                    if board.board[i][j+1].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                if (i < board.boardSize - 1 and j < board.boardSize - 1):
                    if board.board[i+1][j+1].selected == False:
                        #print("in statement")
                        count_not_clicked = count_not_clicked + 1
                '''
                #compare cells not selected with this cell's adjacency count
                if count_not_clicked <= board.cell_dict[f"{x},{y}"]["value"]:
                    print("calls mark adjacent 100")
                    mark_all_adjacent_unselected(board, x, y)
    #x, y = AI_move_randomly(board.boardSize)
    #while board.board[x][y].probability == 1 or board.board[x][y].selected:
        #print("repicked")
    #    x, y = AI_move_randomly(board.boardSize)
    #print("chose: ", x, y)
    #return x, y

def AI_chooses_0s_but_not_100s(Board):
    AI_checks_100s(Board)
    AI_checks_0s(Board)
    zeroChance, definiteChance = checkProbabilities(Board)
    selections = checks_all_possible_selections(Board)
    print("zeroChance:", zeroChance)
    print("definiteChance:", definiteChance)
    print("selectioncs:", selections)

    if zeroChance:
        randomCell = random.randint(0, len(zeroChance) - 1)
        x, y = zeroChance[randomCell]
        print("here: ", x, ":", y)


    #finds if a cell with 0% chance exists that has not been selected yet

    #if no such cell exists above, chooses a random cell until it finds one that is unselected without 100% chance
    else:
        print("no zero chance yet")
        for i in definiteChance:
            if i in selections:
                selections.remove(i)
        randomCell = random.randint(0, len(selections) - 1)
        x, y = selections[randomCell]
        if x == 0 and y == 0:
            x = 1

    return x, y


# print("chose: ", x, y)
# return x, y


def checkProbabilities(Board):
    probability0 = []
    probability100 = []
    for i in range(0, Board.width):
        for j in range(0, Board.height):
            print("for loop:", Board.cell_dict[f"{i},{j}"]["probability"])
            if Board.cell_dict[f"{i},{j}"]["probability"] == 0 and not Board.cell_dict[f"{i},{j}"]["selected"]:
                print("should append 0")
                probability0.append([i, j])
            if Board.cell_dict[f"{i},{j}"]["probability"] == 1 and not Board.cell_dict[f"{i},{j}"]["selected"]:
                print("should append 100")
                probability100.append([i, j])
    #print(probability0)
    return probability0, probability100





def mark_all_adjacent_unselected(Board, x, y):
    cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                      f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]

    for neighbor in cell_neighbors:
        if neighbor in Board.cell_dict.keys():
            if not Board.cell_dict[neighbor]["selected"]:
                print("sets probability to 1")
                Board.cell_dict[neighbor]["probability"] = 1





    '''
    #print("marked all for", i, j)
    if (i > 0 and j > 0):
        if Board.board[i - 1][j - 1].selected == False:
            Board.board[i - 1][j - 1].probability = 1
    if (j > 0):
        if Board.board[i][j - 1].selected == False:
            Board.board[i][j - 1].probability = 1
    if (i < Board.boardSize - 1 and j > 0):
        if Board.board[i + 1][j - 1].selected == False:
           Board.board[i + 1][j - 1].probability = 1
    if (i > 0):
        if Board.board[i - 1][j].selected == False:
            Board.board[i - 1][j].probability = 1
    if (i < Board.boardSize - 1):
        if Board.board[i + 1][j].selected == False:
            Board.board[i + 1][j].probability = 1
    if (i > 0 and j < Board.boardSize - 1):
        if Board.board[i - 1][j + 1].selected == False:
            Board.board[i - 1][j + 1].probability = 1
    if (j < Board.boardSize - 1):
        if Board.board[i][j + 1].selected == False:
            Board.board[i][j + 1].probability = 1
    if (i < Board.boardSize - 1 and j < Board.boardSize - 1):
        if Board.board[i + 1][j + 1].selected == False:
            Board.board[i + 1][j + 1].probability = 1
            '''



def checks_all_possible_selections(Board):
    canBeSelected = []
    for i in range(0, Board.width):
        for j in range(0, Board.height):
            if not Board.cell_dict[f"{i},{j}"]["selected"]:
                canBeSelected.append([i, j])
    return canBeSelected