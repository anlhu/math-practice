import tkinter as tk
from screens import MenuPage, GamePage

class App(tk.Tk):
	 
	def __init__(self): 
		tk.Tk.__init__(self)
		 
		container = tk.Frame(self)  
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		for pageClass in (MenuPage, GamePage):
			frame = pageClass(container, self)
			self.frames[pageClass] = frame 
			frame.grid(row = 0, column = 0, sticky ="nsew")
  
		self.show_frame(MenuPage)
  
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

app = App()
app.mainloop()