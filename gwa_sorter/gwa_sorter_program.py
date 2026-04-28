# import custom tkinter
import customtkinter as ctk

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

# dictionary to be used
        self.gwa_dict = {}

# button to open a window to ask for user input

## ask for user input to put 20 gwa with their names

# button to show the name(s) with the highest gwa
if __name__ == "__main__":
    main_app = MainApp()
    main_app.mainloop()