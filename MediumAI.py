import math

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
    reset_probabilities(Board)
    AI_checks_100s(Board)
    AI_checks_0s(Board)
    print("before check")

    print("after check")
    zeroChance, definiteChance = checkProbabilities(Board)
    if not zeroChance:
        check_rest_probabilities(Board)
    selections = checks_all_possible_selections(Board)

    AIPlacedBombs = Board.AIplaced  # checkKnown(Board)
    for i in AIPlacedBombs:
        print("probability:", Board.cell_dict[f"{i[0]},{i[1]}"]["probability"])
        Board.cell_dict[f"{i[0]},{i[1]}"]["probability"] = 1
        print("probability:", Board.cell_dict[f"{i[0]},{i[1]}"]["probability"])
        if i in selections:
            selections.remove(i)

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

        for i in definiteChance:
            if i in selections:
                selections.remove(i)
        lowest_possibility = .99
        lowest_possibility_array = []
        for i in selections:
            print("no zero chance yet, i[0], i[1]:", i[0], i[1])
            if Board.cell_dict[f"{i[0]},{i[1]}"]["probability"] < lowest_possibility:
                lowest_possibility = Board.cell_dict[f"{i[0]},{i[1]}"]["probability"]
        for i in selections:
            if Board.cell_dict[f"{i[0]},{i[1]}"]["probability"] == lowest_possibility:
                print("append: ", Board.cell_dict[f"{i[0]},{i[1]}"]["probability"], "to", i[0], ":", i[1],)
                lowest_possibility_array.append([i[0],i[1]])
        randomCell = random.randint(0, len(lowest_possibility_array) - 1)
        print("array:", lowest_possibility_array)
        print("randomCell:", randomCell)
        print("this is lowest:", lowest_possibility_array[randomCell])
        x, y = lowest_possibility_array[randomCell]
        print("got here with:", x, y)

    Board.cell_dict[f"{x},{y}"]["probability"] = 0
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


def check_rest_probabilities(Board):
    nonadjacents = []
    for x in range(0, Board.width):
        for y in range(0, Board.height):
            if Board.cell_dict[f"{x},{y}"]["selected"]:
                adjacent = 0
                cells_100 = 0
                cells_0 = 0

                cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                                  f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]

                for neighbor in cell_neighbors:
                    if neighbor in Board.cell_dict.keys():
                        if not Board.cell_dict[neighbor]["selected"]:
                            adjacent += 1
                        if not Board.cell_dict[neighbor]["selected"] and Board.cell_dict[neighbor]["probability"] == 1:
                            cells_100 += 1
                        if not Board.cell_dict[neighbor]["selected"] and Board.cell_dict[neighbor]["probability"] == 0:
                            cells_0 += 1

                print("adjacent:", adjacent)
                if adjacent == 0:
                    continue
                else:
                    probability_of_rest_adjacents = (Board.cell_dict[f"{x},{y}"]["value"]) / (adjacent)

                for neighbor in cell_neighbors:
                    if neighbor in Board.cell_dict.keys():
                        if not Board.cell_dict[neighbor]["selected"] and not Board.cell_dict[neighbor]["probability"] == 1 and not Board.cell_dict[neighbor]["probability"] == 0:
                            if probability_of_rest_adjacents > Board.cell_dict[neighbor]["probability"]:
                                Board.cell_dict[neighbor]["probability"] = probability_of_rest_adjacents

    nonadjacent = 0
    knownMines = 0         # make all nonadjacent probabilities = nonadjacent cells / nonadjacent mines
    for x in range(0, Board.width):
        for y in range(0, Board.height):
            if not Board.cell_dict[f"{x},{y}"]["selected"] and Board.cell_dict[f"{x},{y}"]["probability"] == 0.01:
                nonadjacent += 1
                #TODO: make sure nonadjacemt cant be 0

                # if probability not updated since this turn
                # if not selected and has no selected adjacents
                nonadjacents.append([x, y])
            elif not Board.cell_dict[f"{x},{y}"]["selected"] and Board.cell_dict[f"{x},{y}"]["probability"] == 1:
                knownMines += 1
    for cell in nonadjacents:
        print("ceLL: ", cell)
        print(nonadjacent - 1)
        print((((2*len(Board.AIplaced)) - knownMines)-1))
        print((math.comb((nonadjacent - 1), (((2*len(Board.AIplaced)) - knownMines)-1))))
        print(":")
        print(math.comb(nonadjacent, ((2*len(Board.AIplaced)) - knownMines)))
        Board.cell_dict[f"{cell[0]},{cell[1]}"]["probability"] = ((math.comb((nonadjacent - 1), (((2*len(Board.AIplaced)) - knownMines)-1))) / math.comb(nonadjacent, ((2*len(Board.AIplaced)) - knownMines))) #nonadjacent / (len(Board.AIplaced) - knownMines)


def reset_probabilities(Board):
    for x in range(0, Board.width):
        for y in range(0, Board.height):
            if not Board.cell_dict[f"{x},{y}"]["selected"]:
                Board.cell_dict[f"{x},{y}"]["probability"] = 0.01

def checks_all_possible_selections(Board):
    canBeSelected = []
    for i in range(0, Board.width):
        for j in range(0, Board.height):
            if not Board.cell_dict[f"{i},{j}"]["selected"]:
                canBeSelected.append([i, j])
    return canBeSelected