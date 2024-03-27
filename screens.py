import tkinter as tk
from tkinter import ttk
from question_generator import QuestionGenerator

class MenuPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.config(background="gray64")

		self.pack()
		
		title_label = tk.Label(self, text="Math Practice", font=("Helvetica", 24))
		title_label.pack(pady=20)

		for category in self.controller.categories:
			categoryLabel = tk.Label(self, text=category, font=("Helvetica", 20))
			categoryLabel.pack(pady=10)
			for difficulty in ["Basic", "Advanced"]:
				checkbox = tk.Checkbutton(self, text=difficulty,variable=self.controller.selections[difficulty+category], onvalue=1, offvalue=0, command=lambda difficulty=difficulty, category=category: print(self.controller.selections[difficulty+category], self.controller.selections[difficulty+category].get()))
				checkbox.pack(pady=1)

		command = lambda : self.controller.reset_game() or self.controller.show_frame(GamePage)
		start_button = tk.Button(self, text="Start", font=("Helvetica", 20), command=command)
		start_button.pack(pady=20)


class GamePage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		self.questionGen = QuestionGenerator(controller.categories, controller.selections)
		self.controller = controller
		self.config(background="gray64")

		title_label = tk.Label(self, text="Math Practice", font=("Helvetica", 24))
		title_label.pack(pady=20)

		command = lambda : self.controller.show_frame(MenuPage)
		start_button = tk.Button(self, text="Back", font=("Helvetica", 10), command=command)
		start_button.pack(pady=10)

		self.previous_problem = ""
		self.current_problem = ""
		self.next_problem = ""
	