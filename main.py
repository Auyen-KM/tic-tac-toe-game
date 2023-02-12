import customtkinter as ct
import random
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")
counter = [0, 0]


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.end = False
        self.title("Tic Tac Toe")
        self.geometry("500x550+600+100")

        self.label = ct.CTkLabel(
            master=self, text="Wanna play Tic-Tac-Toe with computer? Go ahead, you start.", pady=50)
        self.label.pack()
        self.frame = ct.CTkFrame(
            master=self, width=500, height=500, fg_color="#a52f9d")
        self.frame.pack(pady=(0, 30), padx=40)

        # [print(i) for i in self.frame.winfo_children()]
        # for i in range(3):
        #     for j in range(3):

        #         b[i][j] = ct.CTkButton(master=self.frame, height=4, width=8, font=(
        #             "Helvetica", "20"), command=(lambda r=i, c=j: self.clicked(r, c)))
        #         b[i][j].grid(row=i, column=j)
        # self.s = []
        for i in range(3):
            for j in range(3):
                self.creating_field(f"button{i}{j}", i, j)
        self.restart_button = ct.CTkButton(
            master=self, text='restart', command=self.restart)
        self.restart_button.pack()

    def creating_field(self, name, i, j):
        name = ct.CTkButton(
            master=self.frame, width=100, text="", font=("", 50), height=100, fg_color='#2FA572', text_color_disabled="white", command=lambda: self.move(name))
        name.grid(row=i, column=j, pady=3, padx=3)

    def restart(self):
        self.restart_button.configure(text="restart")
        for i in self.frame.winfo_children():
            i.configure(text="", state="normal")
        self.end = False

    def disable_all(self):
        for i in self.frame.winfo_children():
            i.configure(state="disabled")

    def check(self):
        s = []
        for i in self.frame.winfo_children():
            s.append(i.cget("text"))
        win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        if not '' in s:
            self.restart_button.configure(text=f"It's tie. Restart?")
            self.end = True
            self.disable_all()

        for i in win:
            if s[i[0]] == s[i[1]] == s[i[2]] and s[i[0]] != "":
                if s[i[0]] == "❌":
                    self.restart_button.configure(
                        text=f"You win! Restart?")
                else:
                    self.restart_button.configure(
                        text=f"You lost! Restart?")
                self.disable_all()
                break

    def computer_move(self):
        if not self.end:
            while (r := random.choice(self.frame.winfo_children())).cget("text") != "":
                r = random.choice(self.frame.winfo_children())
            r.configure(text="⭕", state="disabled")

    def move(self, button):
        button.configure(text="❌", state="disabled")
        self.check()
        self.computer_move()
        self.check()


if __name__ == "__main__":
    app = App()
    app.mainloop()
