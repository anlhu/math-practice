import tkinter as tk
from tkinter import ttk
from question_generator import QuestionGenerator
from PIL import Image, ImageDraw
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\andre\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

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

		reset_game = lambda : self.controller.reset_game_frame() or self.controller.show_frame(GamePage)
		start_button = tk.Button(self, text="Start", font=("Helvetica", 20), command=reset_game)
		start_button.pack(pady=20)


class GamePage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		self.questionGen = QuestionGenerator(controller.categories, controller.selections)
		self.controller = controller
		self.config(background="gray64")

		title_label = tk.Label(self, text="Math Practice", font=("Helvetica", 24))
		title_label.pack(pady=20)

		back_to_menu = lambda : self.controller.show_frame(MenuPage)
		start_button = tk.Button(self, text="Back", font=("Helvetica", 10), command=back_to_menu)
		start_button.pack(pady=10)

		self.problem, self.answer = self.questionGen.getQuestionAndAnswer()
		question = tk.Label(self, text=self.problem+" =", font=("Helvetica", 72))
		question.pack(pady=80)

		reset_game = lambda : self.controller.reset_game_frame() or self.controller.show_frame(GamePage)
		next_button = tk.Button(self, text="Next", font=("Helvetica", 20), command=reset_game)
		next_button.pack(pady=20)

		canvas = tk.Canvas(self, bg="white")
		canvas.pack()
		canvas.update()
		self.canvasImage = Image.new("RGB", (int(canvas['width']), int(canvas['height'])), "white") # may need fixed for ML model

		self.imageDrawing = ImageDraw.Draw(self.canvasImage)
		def get_position(event):
			global last_x, last_y
			last_x, last_y = event.x, event.y
		def draw(event):
			global last_x, last_y
			canvas.create_line(last_x, last_y, event.x, event.y, width=3)
			self.imageDrawing.line([last_x, last_y, event.x, event.y], fill="black", width=5)
			get_position(event)
		canvas.bind("<Button-1>", get_position)
		canvas.bind("<B1-Motion>", draw)

		def verifyAnswerImage():
			written_answer = pytesseract.image_to_string(self.canvasImage, config='--psm 6')
			self.canvasImage.save('answer_drawing.png')
			print(written_answer.strip())
			if written_answer.strip() == str(self.answer):
				reset_game()
			else:
				canvas.delete("all")
				self.canvasImage = Image.new("RGB", (int(canvas['width']), int(canvas['height'])), "white")
				self.imageDrawing = ImageDraw.Draw(self.canvasImage)

		submit_answer = verifyAnswerImage
		submit_button = tk.Button(self, text="Submit", font=("Helvetica", 20), command=submit_answer)
		submit_button.pack(pady=20)

		# TODO
		# maybe add some kind of timer to it
