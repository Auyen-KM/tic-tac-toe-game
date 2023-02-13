import customtkinter as ct
import random
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")
counter = [0, 0]
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
       (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
variations = (
    (0, 1, 2), (0, 2, 1), (2, 1, 0),        # horizontal
    (3, 4, 5), (3, 5, 4), (4, 5, 3),
    (6, 7, 8), (6, 8, 7), (7, 8, 6),
    (0, 3, 6), (0, 6, 3), (3, 6, 0),        # vertical
    (1, 4, 7), (1, 7, 4), (4, 7, 1),
    (2, 5, 8), (2, 8, 5), (5, 8, 2),
    (0, 4, 8), (0, 8, 4), (4, 8, 0),        # diagonal
    (2, 4, 6), (2, 6, 4), (4, 6, 2),

)


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.end = False
        self.title("Tic Tac Toe")
        self.geometry("500x550+600+100")
        self.score = [0, 0]

        self.label = ct.CTkLabel(
            master=self, text="Wanna play Tic-Tac-Toe with computer? Go ahead, you start.", pady=50, font=("Roboto", 16))
        self.label.pack()
        self.frame = ct.CTkFrame(
            master=self, width=500, height=500, fg_color="#a52f9d")
        self.frame.pack(pady=(0, 30), padx=40)
        for i in range(3):
            for j in range(3):
                self.creating_field(f"button{i}{j}", i, j)
        self.restart_button = ct.CTkButton(
            master=self, text='restart', command=self.restart)
        self.restart_button.pack()
        self.iscomputermoved = False

    def creating_field(self, name, i, j):
        name = ct.CTkButton(
            master=self.frame, width=100, text="", font=("", 50), height=100, fg_color='#2FA572', text_color_disabled="white", command=lambda: self.move(name))
        name.grid(row=i, column=j, pady=3, padx=3)

    def restart(self):
        self.restart_button.configure(text="Restart")
        for i in self.frame.winfo_children():
            i.configure(text="", state="normal")
        self.end = False
        self.label.configure(
            text=f"Your's score {self.score[0]} : {self.score[1]} Computer's score")

    def disable_all(self):
        for i in self.frame.winfo_children():
            i.configure(state="disabled")

    def check(self):
        s = []
        for i in self.frame.winfo_children():
            s.append(i.cget("text"))
        if not '' in s:
            self.restart_button.configure(text=f"It's tie. Restart?")
            self.end = True
            self.disable_all()
        for i in win:
            if s[i[0]] == s[i[1]] == s[i[2]] == "❌":
                self.restart_button.configure(
                    text=f"You win! Restart?")
                self.score[0] += 1
                self.end = True
                self.disable_all()
                return
        if not self.end:

            if not self.iscomputermoved:
                self.computer_move()
                self.iscomputermoved = True
                self.check()
            else:
                self.iscomputermoved = False

    def computer_move(self):
        s = []
        move = ''
        find_move = False
        for i in self.frame.winfo_children():
            if i.cget("text") == "":
                s.append(".")
            else:
                s.append(i.cget("text"))
        for i in variations:
            if s[i[0]] == s[i[1]] == "⭕" and s[i[2]] == ".":
                move = i[2]
                find_move = True
                break
        else:
            for j in variations:
                if s[j[0]] == s[j[1]] == "❌" and s[j[2]] == ".":
                    move = j[2]
                    find_move = True
                    break
        if find_move:
            for j, i in enumerate(self.frame.winfo_children()):
                if i.cget("text") == '' and j == move:
                    i.configure(text="⭕", state="disabled")
                    break
        else:
            while (r := random.choice(self.frame.winfo_children())).cget("text") != "":
                r = random.choice(self.frame.winfo_children())
            r.configure(text="⭕", state="disabled")
        s = []
        for i in self.frame.winfo_children():
            s.append(i.cget("text"))
        for i in win:
            if s[i[0]] == s[i[1]] == s[i[2]] == "⭕":
                self.restart_button.configure(
                    text=f"You lost! Restart?")
                self.score[1] += 1
                self.disable_all()
                return

    def move(self, button):
        button.configure(text="❌", state="disabled")
        self.check()


if __name__ == "__main__":
    app = App()
    app.mainloop()
