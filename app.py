import tkinter as tk
from screens import MenuPage, GamePage

class App(tk.Tk):
	 
	def __init__(self): 
		tk.Tk.__init__(self)
		 
		self.container = tk.Frame(self)  
		self.container.pack(side = "top", fill = "both", expand = True) 
		self.container.grid_rowconfigure(0, weight = 1)
		self.container.grid_columnconfigure(0, weight = 1)
		
		self.categories = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Root Extraction"]
		self.selections = {difficulty+category : tk.IntVar() for category in self.categories for difficulty in ["Basic", "Advanced"]}

		self.frames = {}

		for pageClass in (MenuPage, GamePage):
			frame = pageClass(self.container, self)
			self.frames[pageClass] = frame 
			frame.grid(row = 0, column = 0, sticky ="nsew")
  
		self.show_frame(MenuPage)
  
	def show_frame(self, nextFrame):
		frame = self.frames[nextFrame]
		frame.tkraise()

	def reset_game(self):
		del self.frames[GamePage]
		self.frames[GamePage] = GamePage(self.container, self)
		self.frames[GamePage].grid(row = 0, column = 0, sticky ="nsew")