import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("500x550+600+100")
        self.frame = ct.CTkFrame(master=self, width=400, height=400)
        self.frame.pack(pady=30, padx=40)
        self.field_button = ct.CTkButton(master=self.frame)
        self.field_button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
