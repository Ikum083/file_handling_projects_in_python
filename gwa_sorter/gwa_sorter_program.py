# import custom tkinter
import customtkinter as ctk
import json

# json file to be used
try:
    with open("gwa.json", "r") as file:
        gwa_dict = json.load(file)
except json.JSONDecodeError:
    gwa_dict = {}

# setup main class
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

# setup custom tkinter window
        self.window_size = "800x600"
        self.geometry(self.window_size)
        self.title("GWA Sorter")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0, 1), weight = 1)

# button to open a window to ask for user input
        self.button_sizes_main_menu_x = 480
        self.button_sizes_main_menu_y = 80

        self.gwa_input = ctk.CTkButton(self, text = "Input GWA", width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, font = ("Arial", 40))
        self.gwa_input.grid(row = 0, column = 0)
        
        self.highest_gwa = ctk.CTkButton(self, text = "Highest GWA", width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, font = ("Arial", 40))
        self.highest_gwa.grid(row = 1, column = 0)

## ask for user input to put 20 gwa with their names
    def user_input_gwa(self, gwa_dict):
        input_gwa_window = ctk.CTkToplevel(self)

        enter_gwa = ctk.CTkEntry()

# button to show the name(s) with the highest gwa
if __name__ == "__main__":
    main_app = MainApp()
    main_app.mainloop()