# import custom tkinter
import customtkinter as ctk
import json

# json file to be used
try:
    with open("gwa_sorter/gwa.json", "r") as file:
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

        self.gwa_input = ctk.CTkButton(self, text = "Input GWA", width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, font = ("Arial", 40), command = lambda : self.user_input_gwa(gwa_dict))
        self.gwa_input.grid(row = 0, column = 0)
        
        self.highest_gwa = ctk.CTkButton(self, text = "Highest GWA", width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, font = ("Arial", 40))
        self.highest_gwa.grid(row = 1, column = 0)

## ask for user input to put 20 gwa with their names
    def user_input_gwa(self, gwa_dict):
        input_gwa_window = ctk.CTkToplevel(self)
        input_gwa_window.geometry(self.window_size)
        input_gwa_window.title("Input GWA")
        input_gwa_window.attributes("-topmost", True)
        input_gwa_window.grid_columnconfigure((0, 2), weight = 1)
        input_gwa_window.grid_rowconfigure(0, weight = 1)

        enter_gwa = ctk.CTkEntry(input_gwa_window, placeholder_text = "", width = 300, height = 70, font = ("Arial", 30))
        enter_gwa.grid(row = 0, column = 0)

        enter_name = ctk.CTkEntry(input_gwa_window, placeholder_text = "", width = 300, height = 70, font = ("Arial", 30))
        enter_name.grid(row = 0, column = 1)

        enter_into_file = ctk.CTkButton(input_gwa_window, text = "+", font = ("Arial", 40), width = 70, height = 70)
        enter_into_file.grid(row = 0, column = 2)

        gwa_label = ctk.CTkLabel(input_gwa_window, text = "GWA", font = ("Arial", 30), text_color = "White")
        gwa_label.place(x = 140, y = 190)

        name_label = ctk.CTkLabel(input_gwa_window, text = "Name", font = ("Arial", 30), text_color = "White")
        name_label.place(x = 480, y = 190)

# button to show the name(s) with the highest gwa
if __name__ == "__main__":
    main_app = MainApp()
    main_app.mainloop()