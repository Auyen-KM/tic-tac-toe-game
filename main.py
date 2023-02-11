import customtkinter as ct


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("500x400+800+300")


if __name__ == "__main__":
    app = App()
    app.mainloop()
