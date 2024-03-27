import tkinter as tk
from tkinter import ttk

class MenuPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.config(background="gray64")
		
		self.categories = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Root Extraction"]
		self.selections = {difficulty+category : tk.IntVar() for category in self.categories for difficulty in ["Basic", "Advanced"]}

		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.title_label = tk.Label(self, text="Math Practice", font=("Helvetica", 24))
		self.title_label.pack(pady=20)

		for category in self.categories:
			categoryLabel = tk.Label(self, text=category, font=("Helvetica", 20))
			categoryLabel.pack(pady=10)
			for difficulty in ["Basic", "Advanced"]:
				checkbox = tk.Checkbutton(self, text=difficulty,variable=self.selections[difficulty+category], onvalue=1, offvalue=0)
				checkbox.pack(pady=1)

		command = lambda : self.controller.show_frame(GamePage)
		self.addition_button = tk.Button(self, text="Start", font=("Helvetica", 20), command=command)
		self.addition_button.pack(pady=20)

class GamePage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text ="Game Page")
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="Menu Page",
		command = lambda : controller.show_frame(MenuPage))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)