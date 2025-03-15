'''
from EasyAI import checks_all_possible_selections
from main import *
import math

def check_if_selected_adjacent_cell(Board):
    adjacency = []
    for i in range(0, Board.boardSize):
        for j in range(0, Board.boardSize):
            count_selected = 0

            if not Board.board[i][j].selected:
                # print("I got selected: ", i, j)
                # compare surrounding cells
                if (i > 0 and j > 0):
                    if Board.board[i - 1][j - 1].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (j > 0):
                    if Board.board[i][j - 1].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (i < Board.boardSize - 1 and j > 0):
                    if Board.board[i + 1][j - 1].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (i > 0):
                    if Board.board[i - 1][j].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (i < Board.boardSize - 1):
                    if Board.board[i + 1][j].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (i > 0 and j < Board.boardSize - 1):
                    if Board.board[i - 1][j + 1].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (j < Board.boardSize - 1):
                    if Board.board[i][j + 1].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
                if (i < Board.boardSize - 1 and j < Board.boardSize - 1):
                    if Board.board[i + 1][j + 1].selected == True:
                        # print("in statement")
                        count_selected = count_selected + 1
            if count_selected > 0:
                adjacency.append([i, j])
    return adjacency

def place_mine(Board):
    adjacent = check_if_selected_adjacent_cell(Board)
    mineCount -= 1
    if mineCount == 0:
        listOfAdjacentSolutions.append()
    else:
        place_mine


def HardAIBase(Board):
    #adjacent math
    #do math to determine possible configs of mines in adjacent cells


    #rest math
    selections = checks_all_possible_selections(Board)
    allNeutral = selections
    for i in adjacent:
        if i in allNeutral:
            allNeutral.remove(i)
    totalNeutralCells = len(allNeutral)
    minesLeft = Board.numMines - knownMines
    combinations = math.comb(totalNeutralCells, minesLeft)
'''