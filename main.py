from PIL import Image
import customtkinter as ctk
ctk.set_appearance_mode("dark")


class Board(object):
    def __init__(self):
        self.width = 0
        self.height = "no"
        self.selectable_spaces = 0
        self.selectable_list = []
        self.cell_dict = {}
        self.mine_GUI = ""

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

    def clear_board(self):
        for widget in tabview.tab("Main").winfo_children():
            widget.destroy()

    def cell_clicked(self, x, y):
        cell = self.cell_dict[f"{x},{y}"]
        square_button = get_widget_at_location_grid(self.mine_GUI, x, y)
        if cell["mine"] > 0:
            square_button.configure(image=square_bomb, state="disabled")
            print("Game Over")
        else:
            square_button.configure(image=image_map[str(cell["value"])], state="disabled")
        cell["selected"] = True


    def set_cell_values(self):
        for cell in self.cell_dict.keys():
            pos = cell.split(",")
            x = int(pos[0])
            y = int(pos[1])
            cell_neighbors = [f"{x+1},{y}", f"{x+1},{y+1}", f"{x+1},{y-1}", f"{x-1},{y}",
                              f"{x-1},{y+1}", f"{x-1},{y-1}", f"{x},{y+1}", f"{x},{y-1}"]
            num_adjacent_mines = 0
            print(x, y)
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

w = ctk.CTk()


def start_generating():
    width_widget = setup_frame.winfo_children()[0]
    height_widget = setup_frame.winfo_children()[1]
    game_board = Board()
    game_board.width = int(width_widget.get())
    game_board.height = int(height_widget.get())
    #set height and width
    game_board.make_board()
    game_board.place_mine(0,0)

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
width_label = ctk.CTkLabel(setup_frame, text="Width:")
height_label = ctk.CTkLabel(setup_frame, text="Height:")
bomb_label = ctk.CTkLabel(setup_frame, text="# of Mines:")

generate_button = ctk.CTkButton(setup_frame, text="Generate Grid", command=start_generating)

width_entry.grid(row=0, column=1, sticky="nsew")
height_entry.grid(row=1, column=1, sticky="nsew")
width_label.grid(row=0, column=0, sticky="nsew")
height_label.grid(row=1, column=0, sticky="nsew")
bomb_entry.grid(row=2, column=1, sticky="nsew")
bomb_label.grid(row=2, column=0, sticky="nsew")
generate_button.grid(row=3, column=0, columnspan=2, sticky="nsew")
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
