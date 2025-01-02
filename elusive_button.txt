"""
Title: Elusive Button
Author: Paul King
Date: 12-22-2024
Description: Program makes an offer you can't refuse.
"""


import tkinter as tk
import random
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proposal")
        self.geometry("400x300")

        self.question_label = tk.Label(self, text="I think we need Christmas Tamales?")
        self.question_label.pack(pady=10)

        self.yes_button = tk.Button(self, text="Yes", command=self.yes_button_clicked)
        self.yes_button.pack(pady=20, side="left", padx=30)

        self.no_button = tk.Button(self, text="No")
        self.no_button.pack(pady=20, side="left")
        self.no_button.place(x=150, y=150)

        self.no_button.bind("<Enter>", self.move_no_button)

    def yes_button_clicked(self):
        tk.messagebox.showinfo("Response", "Awww, thank you!")

    def move_no_button(self, event):
        x = random.randint(0, self.winfo_width() - self.no_button.winfo_width())
        y = random.randint(0, self.winfo_height() - self.no_button.winfo_height())
        self.no_button.place(x=x, y=y)

if __name__ == "__main__":
    app = App()
    app.mainloop()
