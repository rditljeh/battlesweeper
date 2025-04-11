import itertools
import random
from collections import Counter
from operator import itemgetter
import math
import time


def set_constraints(board):
    # will return a list of constraints with the format [number of mines present, [cell_candiate1, cell_candiate2, ..]
    constraint_list = []
    cells_of_interest = []
    for x in range(0, board.width):
        for y in range(0, board.height):
            cell = board.cell_dict[f"{x},{y}"]
            if cell["selected"]:

                cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                                  f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]
                options = []

                for neighbor in cell_neighbors:
                    print(neighbor)
                    if neighbor in board.cell_dict.keys() and board.cell_dict[neighbor]["selected"] == False:
                        options.append(neighbor)
                        #options.append(neighbor)
                        cells_of_interest.append(neighbor)
                numb_possibilities = math.comb(len(options), cell["value"])
                constraint_list.append([cell["value"], options, numb_possibilities])
    #adding self-placed as a constraint
    #constraint_list.append([self.player_to_place, self.AIplaced, math.comb(len(self.AIplaced), self.player_to_place)])

    # keeps only unique cells
    board.cells_of_interest = list(set(cells_of_interest))
    #constraint_list.sort(key=lambda x: x[2])
    board.constraints = constraint_list
    print("CONSTRAINT:", constraint_list)
    #print(constraint_list)
    #return constraint_list, cells_of_interest

def legal_check(board, depth, lethal_cells):

    for c in range(0, depth+1):
        constraint = board.constraints[c]

        num_matches = 0
        for cell in constraint[1]:
            if cell in lethal_cells:
                num_matches += lethal_cells.count(cell)
        if num_matches != constraint[0]:
            return False

    return True

def recursive_check(board, depth, lethal_cells):
    #print(depth, self.legal_states, (self.constraints))
    # check if the constraint is already satisfied
    if legal_check(board, depth, lethal_cells):
        if depth+1 >= len(board.constraints):
            # sometimes duplicates are chosen
            board.legal_states.append(lethal_cells)
        else:
            recursive_check(board, depth + 1, lethal_cells)
    new_possibilities = list(itertools.combinations(board.constraints[depth][1], board.constraints[depth][0]))
    for cell in board.constraints[depth][1]:
        new_possibilities.append([cell,cell])
    for p in new_possibilities:
        # store choices in temp to compare against constraints
        temp = lethal_cells + list(p)
        if legal_check(board, depth, temp):
            if depth+1 == len(board.constraints):
                # sometimes duplicates are chosen
                #self.legal_states.append(list(set(temp)))
                board.legal_states.append(temp)
            else:
                recursive_check(board, depth + 1, temp)


def generate_possible_boards(board):
    board.legal_states = []
    set_constraints(board)
    depth = 0
    num_mines = board.constraints[depth][0]
    initial_possibilites = list(itertools.combinations(board.constraints[depth][1], num_mines))
    for cell in board.constraints[depth][1]:
        initial_possibilites.append([cell,cell])
    print("starting checks")
    for p in initial_possibilites:
        recursive_check(board, depth, list(p))
    print("finished checks")
    print(board.legal_states)
    print(len(board.legal_states))
    x, y = count_occurences(board, board.legal_states)
    return int(x), int(y)

def final_unknown_prob(board, legal_states):
    length_total = 0
    for state in legal_states:
        length_total += len(state)
    avg_found_mines = length_total/len(legal_states)
    total_mines = len(board.AIplaced) * 2
    unknown_mines = total_mines-avg_found_mines
    if unknown_mines <= 0:
        # checking if all cells have known neighbors
        return 101, []
    unknown_cells = []
    for cell in board.cell_dict.keys():
        if not board.cell_dict[cell]["selected"] and cell not in board.cells_of_interest and cell not in board.AIplaced:
            unknown_cells.append(cell)

    unknown_percent = unknown_mines/len(unknown_cells)*100
    print(f"UNKNOWN CHECK: {len(unknown_cells)} cells, {unknown_mines} mines")
    return unknown_percent, unknown_cells

def count_occurences(board, lists):
    all_possibilities = []
    print("AI bombs", board.AIplaced)
    for lst in lists:
        all_possibilities.extend(lst)
    counts = Counter(all_possibilities)
    for cell in counts:
        board.cell_dict[cell]["probability"] = (counts[cell]/len(lists)*100)
    for mine in board.AIplaced:
        print(f"{mine[0]},{mine[1]}")
        counts[f"{mine[0]},{mine[1]}"] = 999999
    for cell in board.cells_of_interest:
        if cell not in counts.keys() and cell not in board.AIplaced:
            coords = cell.split(",")
            print(f"GUARANTEED SAFE:{coords}")
            return coords[0], coords[1]
    min_key, min_count = min(counts.items(), key=itemgetter(1))
    #print(f"Lowest probability is {min_key} with {min_count}/{len(lists)} ({(min_count/len(lists))*100}%)")
    print(counts)
    #print(f"INTEREST:{board.cells_of_interest}")
    min_known_percent = (min_count/len(lists))*100
    unknown_percent, unknown_cells = final_unknown_prob(board, lists)
    print("UNKOWN PERCENT", unknown_percent)
    print("MIN KNOWN PERCENT", min_known_percent)
    if unknown_percent > min_known_percent:
        coords = min_key.split(",")
        print(f"LOWEST RISK:{coords}")
        return coords[0], coords[1]
    else:
        coords = random.choice(unknown_cells).split(",")
        print(f"UNKNOWN CELL:{coords}")
        return coords[0], coords[1]



#print(get_constraints(game_board))
