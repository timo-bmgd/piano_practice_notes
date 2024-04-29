import tkinter as tk;
from random import Random

def update_question_label():
    question_label.configure(text=q.next())
    number_label.configure(text=q.index + 1)

class Questions:
    orderby = ""
    index = 0
    question = None

    def __init__(self, name, order="inorder"):
        self.name = name
        self.file = open(self.name + ".txt", "r")
        self.question = self.file.readlines()
        self.orderby = order

    def next(self):
        if self.orderby and self.orderby == "random":
            return self.pick_random()
        else:
            return self.pick_inorder()

    def pick_random(self):
        self.index = Random().randint(0, len(self.question) - 1)
        return self.question[self.index]

    def pick_inorder(self):
        self.index += 1
        return self.question[self.index]


q = Questions("partner")

root = tk.Tk()

root.geometry("500x500")
root.title("Fragen-Reise")
root.configure(background="pink")

number_label = tk.Label(root, text="0", bg="pink")
question_label = tk.Label(root, text="Press Next", font=('Helvetica', 18), bg="pink", wraplength=400)
next_button = tk.Button(root, text="Next", command=update_question_label, bg="pink", highlightbackground="pink")

number_label.pack(padx=5, pady=5, side='left')
question_label.pack(padx=20, pady=40, anchor='center')
next_button.pack(padx=20, pady=20, side='bottom')

root.mainloop()
