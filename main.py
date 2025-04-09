import time
import random
import itertools
from collections import Counter
from operator import itemgetter
import math

from PIL import Image
import customtkinter as ctk

import EasyAI
import AIPickLocations
import MediumAI

ctk.set_appearance_mode("dark")

"""
def play():

    #loop
        #player turn
        #check player lost
        #ai turn
    if game_board.player_to_place <= 0:
        for i in range(0, len(game_board.selectable_list)):
            x, y = MediumAI.AI_chooses_0s_but_not_100s(game_board)     #EasyAI.AI_move_randomly(game_board)
            result = game_board.cell_clicked(x, y)
            if result:
                break
            time.sleep(2)
"""

class Board(object):
    def __init__(self):
        self.width = 0
        self.height = "no"
        self.cells_of_interest = None
        self.constraints = None
        self.legal_states = []
        self.selectable_spaces = 0
        self.selectable_list = []
        self.cell_dict = {}
        self.mine_GUI = ""
        self.AIplaced = []
        self.player_to_place = 0
        self.difficulty = "easy"


    def make_board(self):
        # make board size of width & height
        self.clear_board()
        mine_frame = ctk.CTkFrame(tabview.tab("Main"))
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.cell_dict[f"{x},{y}"] = {"mine":0, "selected":False, "value":0, "probability":0.01}
                self.selectable_list.append(f"{x},{y}")
                button = ctk.CTkButton(master=mine_frame, image=square_base, command=lambda x=x, y=y: self.cell_clicked(x, y),
                                       text="", width=64, height=64)
                button.grid(row=y, column=x, sticky="nsew")
                button.bind("<Button-3>", lambda event, x=x, y=y: self.place_flag(event, x, y))
        self.selectable_spaces = len(self.selectable_list)
        mine_frame.pack()
        self.mine_GUI = mine_frame

    def make_master_view(self):
        master_frame = ctk.CTkFrame(tabview.tab("Master-view"))
        for x in range(0, self.width):
            for y in range(0, self.height):
                cell = self.cell_dict[f"{x},{y}"] #{"mine":0, "selected":False, "value":0, "probability":0.01}
                if cell["mine"] > 0:
                    button = ctk.CTkButton(master=master_frame, image=square_bomb, state="disabled",
                                           text="", width=64, height=64)
                else:
                    button = ctk.CTkButton(master=master_frame, image=image_map[str(cell["value"])], state="disabled",
                                           text="test", width=64, height=64)
                button.grid(row=y, column=x, sticky="nsew")


    def make_bot_view(self):
        # make board size of width & height
        for widget in tabview.tab("Bot-View").winfo_children():
            widget.destroy()
        bot_frame = ctk.CTkFrame(tabview.tab("Bot-View"))
        for x in range(0, self.width):
            for y in range(0, self.height):
                cell = self.cell_dict[f"{x},{y}"]
                label = ctk.CTkLabel(master=bot_frame, text=cell["probability"])
                label.grid(row=y, column=x, sticky="nsew", padx=5, pady=5)
        bot_frame.pack()

    def clear_board(self):
        for widget in tabview.tab("Main").winfo_children():
            widget.destroy()


    def cell_clicked(self, x, y):
        cell = self.cell_dict[f"{x},{y}"]
        square_button = get_widget_at_location_grid(self.mine_GUI, x, y)
        if self.player_to_place > 0:
            self.place_mine(x, y)
            self.player_to_place -= 1
            square_button.configure(image=square_flag_blue)
            if self.player_to_place == 1:
                self.make_master_view()
            return
        if cell["mine"] > 0:
            square_button.configure(image=square_bomb, state="disabled")
            popup = ctk.CTkToplevel(w)
            time.sleep(2)
            popup.title("Game Over")
            label = ctk.CTkLabel(popup, text="Player Lost")
            label.pack(padx=20, pady=20)
            return
        else:
            square_button.configure(image=image_map[str(cell["value"])], state="disabled")
        cell["selected"] = True
        w.update_idletasks()
        if self.difficulty == "Hard":
            self.AIplaced.append([x, y])
        time.sleep(1)
        self.AI_moves()

    def AI_moves(self):
        if self.difficulty == "Easy":
            x, y = EasyAI.AI_move_randomly(game_board)
        elif self.difficulty == "Medium":
            x, y = MediumAI.AI_chooses_0s_but_not_100s(game_board)     #EasyAI.AI_move_randomly(game_board)
        elif self.difficulty == "Hard":
            x, y = game_board.generate_possible_boards()
        self.make_bot_view()
        game_board.AI_cell_clicked(x, y)


    def AI_cell_clicked(self, x, y):
        cell = self.cell_dict[f"{x},{y}"]
        print(f"CELL: {x},{y}: {cell}")
        square_button = get_widget_at_location_grid(self.mine_GUI, x, y)
        if cell["mine"] > 0:
            square_button.configure(image=square_bomb, state="disabled")
            popup = ctk.CTkToplevel(w)
            popup.title("Game Over")
            label = ctk.CTkLabel(popup, text="AI Lost")
            label.pack(padx=20, pady=20)
        else:
            square_button.configure(image=image_map[str(cell["value"])], state="disabled")
        cell["selected"] = True
        w.update_idletasks()



    def set_cell_values(self):
        for cell in self.cell_dict.keys():
            pos = cell.split(",")
            x = int(pos[0])
            y = int(pos[1])
            cell_neighbors = [f"{x+1},{y}", f"{x+1},{y+1}", f"{x+1},{y-1}", f"{x-1},{y}",
                              f"{x-1},{y+1}", f"{x-1},{y-1}", f"{x},{y+1}", f"{x},{y-1}"]
            num_adjacent_mines = 0
            #print(x, y)
            for neighbor in cell_neighbors:
                if neighbor in self.cell_dict.keys():
                    num_adjacent_mines += self.cell_dict[neighbor]["mine"]
            self.cell_dict[cell]["value"] = num_adjacent_mines


    def place_mine(self, x, y):
        #check if loc is legal
        if f"{x},{y}" in self.cell_dict.keys():
            self.cell_dict[f"{x},{y}"]["mine"] += 1
            self.set_cell_values()
        else:
            print("Location is not on grid")


    def place_flag(self, event, x, y):
        square_button = get_widget_at_location_grid(self.mine_GUI, x, y)
        curr_image = square_button.cget("image")
        if square_button.cget("state") != "disabled":
            if curr_image == square_flag:
                square_button.configure(image=square_base)
            else:
                square_button.configure(image=square_flag)

    def set_constraints(self):
        # will return a list of constraints with the format [number of mines present, [cell_candiate1, cell_candiate2, ..]
        constraint_list = []
        cells_of_interest = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                cell = self.cell_dict[f"{x},{y}"]
                if cell["selected"]:

                    cell_neighbors = [f"{x + 1},{y}", f"{x + 1},{y + 1}", f"{x + 1},{y - 1}", f"{x - 1},{y}",
                                      f"{x - 1},{y + 1}", f"{x - 1},{y - 1}", f"{x},{y + 1}", f"{x},{y - 1}"]
                    options = []

                    for neighbor in cell_neighbors:
                        if neighbor in self.cell_dict.keys() and self.cell_dict[neighbor]["selected"] == False:
                            print(neighbor, self.cell_dict[neighbor])
                            options.append(neighbor)
                            #options.append(neighbor)
                            cells_of_interest.append(neighbor)
                    numb_possibilities = math.comb(len(options), cell["value"])
                    constraint_list.append([cell["value"], options, numb_possibilities])
        #adding self-placed as a constraint
        #constraint_list.append([self.player_to_place, self.AIplaced, math.comb(len(self.AIplaced), self.player_to_place)])

        # keeps only unique cells
        self.cells_of_interest = list(set(cells_of_interest))
        #constraint_list.sort(key=lambda x: x[2])
        self.constraints = constraint_list
        #print(constraint_list)
        #return constraint_list, cells_of_interest

    def legal_check(self, depth, lethal_cells):
        """if len(self.constraints) == 1:
            constraint = self.constraints[0]
            num_matches = 0
            for cell in constraint[1]:
                if cell in lethal_cells:
                    num_matches += lethal_cells.count(cell)
            if num_matches != constraint[0]:
                return False
            return True"""
        for c in range(0, depth+1):
            constraint = self.constraints[c]

            num_matches = 0
            for cell in constraint[1]:
                if cell in lethal_cells:
                    num_matches += lethal_cells.count(cell)
            if num_matches != constraint[0]:
                return False

        return True

    def recursive_check(self, depth, lethal_cells):
        #print(depth, self.legal_states, (self.constraints))
        # check if the constraint is already satisfied
        if self.legal_check(depth, lethal_cells):
            if depth+1 == len(self.constraints):
                # sometimes duplicates are chosen
                self.legal_states.append(lethal_cells)
            else:
                self.recursive_check(depth+1, lethal_cells)
        new_possibilities = list(itertools.combinations(self.constraints[depth][1], self.constraints[depth][0]))
        for cell in self.constraints[depth][1]:
            new_possibilities.append([cell,cell])
        for p in new_possibilities:
            # store choices in temp to compare against constraints
            temp = lethal_cells + list(p)
            if self.legal_check(depth, temp):
                if depth+1 == len(self.constraints):
                    # sometimes duplicates are chosen
                    #self.legal_states.append(list(set(temp)))
                    self.legal_states.append(temp)
                else:
                    self.recursive_check(depth+1, temp)


    def generate_possible_boards(self):
        self.set_constraints()
        print(self.constraints)
        depth = 0
        num_mines = self.constraints[depth][0]
        initial_possibilites = list(itertools.combinations(self.constraints[depth][1], num_mines))
        for cell in self.constraints[depth][1]:
            initial_possibilites.append([cell,cell])
        print("starting checks")
        for p in initial_possibilites:
            self.recursive_check(depth, list(p))
        print(f"LEGAL STATES: {self.legal_states}")
        #print(len(self.legal_states))
        x, y = self.count_occurences(self.legal_states)
        print(x,y)
        self.AIplaced.append([x, y])
        return int(x), int(y)

    def final_unknown_prob(self, legal_states):
        length_total = 0
        for state in legal_states:
            length_total += len(state)
        avg_found_mines = length_total/len(legal_states)
        total_mines = self.player_to_place*2
        unknown_mines = total_mines-avg_found_mines
        unknown_cells = []
        for cell in self.cell_dict.keys():
            if not self.cell_dict[cell]["selected"] and cell not in self.cells_of_interest:
                unknown_cells.append(cell)
        if len(unknown_cells) == 0:
            return 101, []
        unknown_percent = unknown_mines/len(unknown_cells)*100
        print(f"UNKNOWN CHECK: {len(unknown_cells)}, {unknown_mines}")
        return unknown_percent, unknown_cells

    def count_occurences(self, lists):
        print("hello?")
        all_possibilities = []
        for lst in lists:
            all_possibilities.extend(lst)
        counts = Counter(all_possibilities)
        print(self.AIplaced)
        for mine in self.AIplaced:
            counts[f"{str(mine[0])},{str(mine[1])}"] = 9999
        if len(self.cells_of_interest) > len(counts.keys()):
            for cell in self.cells_of_interest:
                if cell not in counts.keys() and cell not in self.AIplaced:
                    coords = cell.split(",")
                    print(1, coords)
                    return coords[0], coords[1]
        else:
            min_key, min_count = min(counts.items(), key=itemgetter(1))
            #print(f"Lowest probability is {min_key} with {min_count}/{len(lists)} ({(min_count/len(lists))*100}%)")
            print(counts)
            min_known_percent = (min_count/len(lists))*100
            unknown_percent, unknown_cells = self.final_unknown_prob(lists)
            if unknown_percent > min_known_percent:
                coords = min_key.split(",")
                print(2, coords)
                return coords[0], coords[1]
            else:
                coords = random.choice(unknown_cells).split(",")
                print(3, coords)
                return coords[0], coords[1]

w = ctk.CTk()

game_board = Board()
def start_generating():
    width_widget = setup_frame.winfo_children()[0]
    height_widget = setup_frame.winfo_children()[1]
    bomb_widget = setup_frame.winfo_children()[2]
    difficulty_widget = setup_frame.winfo_children()[3]
    game_board.width = int(width_widget.get())
    game_board.height = int(height_widget.get())
    game_board.player_to_place = int(bomb_widget.get())
    game_board.difficulty = difficulty_widget.get()
    #set height and width
    game_board.make_board()
    tabview.set("Main")
    time.sleep(3)
    AI_mines = AIPickLocations.AI_pick_mines(game_board, int(bomb_widget.get()))
    #place AI mines for it
    for pos in AI_mines:
        game_board.place_mine(pos[0], pos[1])



def get_widget_at_location_grid(parent, x, y):
    for child in parent.winfo_children():
        grid_info = child.grid_info()
        #print(grid_info['row'], grid_info['column'])
        if grid_info['row'] == y and grid_info['column'] == x:
            return child
    return None


# loading images
square_base = ctk.CTkImage(light_image=Image.open("images/Minesweeper_unopened_square.png"), size=(128, 128))
square_bomb = ctk.CTkImage(light_image=Image.open("images/bomb.png"), size=(128, 128))
square_flag = ctk.CTkImage(light_image=Image.open("images/flag.png"), size=(128, 128))
square_flag_blue = ctk.CTkImage(light_image=Image.open("images/flag_blue.png"), size=(128, 128))
square_0 = ctk.CTkImage(light_image=Image.open("images/0.png"), size=(128, 128))
square_1 = ctk.CTkImage(light_image=Image.open("images/1.png"), size=(128, 128))
square_2 = ctk.CTkImage(light_image=Image.open("images/2.png"), size=(128, 128))
square_3 = ctk.CTkImage(light_image=Image.open("images/3.png"), size=(128, 128))
square_4 = ctk.CTkImage(light_image=Image.open("images/4.png"), size=(128, 128))
square_5 = ctk.CTkImage(light_image=Image.open("images/5.png"), size=(128, 128))
square_6 = ctk.CTkImage(light_image=Image.open("images/6.png"), size=(128, 128))
square_7 = ctk.CTkImage(light_image=Image.open("images/7.png"), size=(128, 128))
square_8 = ctk.CTkImage(light_image=Image.open("images/8.png"), size=(128, 128))
square_9 = ctk.CTkImage(light_image=Image.open("images/9.png"), size=(128, 128))
image_map = {"0":square_0,"1":square_1,"2":square_2,"3":square_3,"4":square_4,"5":square_5,"6":square_6,"7":square_7,
             "8":square_8,"9":square_9}

tabview = ctk.CTkTabview(w)
tabview.pack(padx=20, pady=20)

tabview.add("Setup")
tabview.add("Main")
tabview.add("Bot-View")
tabview.add("Master-view")

setup_frame = ctk.CTkFrame(tabview.tab("Setup"))
width_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter a number (ex: 6)")
height_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter a number (ex: 5)")
bomb_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter a number (ex: 4)")
difficulty_dropdown = ctk.CTkOptionMenu(setup_frame, values=["Easy", "Medium", "Hard"])
width_label = ctk.CTkLabel(setup_frame, text="Width:")
height_label = ctk.CTkLabel(setup_frame, text="Height:")
bomb_label = ctk.CTkLabel(setup_frame, text="# of Mines:")
difficulty_label = ctk.CTkLabel(setup_frame, text="Difficulty:")

generate_button = ctk.CTkButton(setup_frame, text="Generate Grid", command=start_generating)

width_entry.grid(row=0, column=1, sticky="nsew")
height_entry.grid(row=1, column=1, sticky="nsew")
width_label.grid(row=0, column=0, sticky="nsew")
height_label.grid(row=1, column=0, sticky="nsew")
bomb_entry.grid(row=2, column=1, sticky="nsew")
bomb_label.grid(row=2, column=0, sticky="nsew")
difficulty_dropdown.grid(row=3, column=1, sticky="nsew")
difficulty_label.grid(row=3, column=0, sticky="nsew")
generate_button.grid(row=4, column=0, columnspan=2, sticky="nsew")
setup_frame.pack()
'''
mine_frame = ctk.CTkFrame(tabview.tab("Main"))
grid_x = 3
grid_y = 3
grid_dict = {}
for x in range(0, grid_x):
    for y in range(0, grid_y):
        button = ctk.CTkButton(master=mine_frame, image=square_base, command=lambda x=x, y=y: square_clicked(x, y),
                               text="", width=128, height=128)
        button.grid(row=y, column=x, sticky="nsew")

mine_frame.pack()
'''

w.mainloop()

