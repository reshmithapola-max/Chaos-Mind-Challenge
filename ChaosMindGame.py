import tkinter as tk
from tkinter import messagebox
import random

class ChaosMindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chaos Mind Challenge")
        self.score = 0

        self.label = tk.Label(root, text="Chaos Mind Challenge", font=("Arial", 18))
        self.label.pack(pady=10)

        self.info = tk.Label(root, text="Click Start")
        self.info.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.btn = tk.Button(root, text="Start", command=self.start_game)
        self.btn.pack(pady=10)

    def start_game(self):
        self.level1()

    def level1(self):
        self.sequence = "".join(str(random.randint(0,9)) for _ in range(5))
        self.info.config(text=f"Memorize: {self.sequence}")
        self.entry.delete(0, tk.END)
        self.btn.config(state="disabled")
        self.root.after(3000, self.ask_level1)

    def ask_level1(self):
        self.info.config(text="Enter the sequence")
        self.btn.config(text="Submit", state="normal", command=self.check_level1)

    def check_level1(self):
        if self.entry.get() == self.sequence:
            self.score += 10
        self.level2()

    def level2(self):
        self.info.config(text="Pattern: 2, 4, 8, 16, ?")
        self.entry.delete(0, tk.END)
        self.btn.config(command=self.check_level2)

    def check_level2(self):
        if self.entry.get().strip() == "32":
            self.score += 10
        self.level3()

    def level3(self):
        self.info.config(text="All but 9 sheep die. How many left?")
        self.entry.delete(0, tk.END)
        self.btn.config(command=self.check_level3)

    def check_level3(self):
        if self.entry.get().strip() == "9":
            self.score += 10
        self.finish()

    def finish(self):
        rank = "Master Mind" if self.score >= 25 else "Sharp Thinker"
        messagebox.showinfo("Game Over", f"Score: {self.score}\nRank: {rank}")
        self.root.destroy()

root = tk.Tk()
app = ChaosMindGame(root)
root.mainloop()
