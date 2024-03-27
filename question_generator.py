import random

class QuestionGenerator():
	def __init__(self, categories, selections) -> None:
		self.categories = categories
		self.selections = selections

		self.possible_selections = []

		for category in self.categories:
			for difficulty in ["Basic", "Advanced"]:
				if selections[difficulty+category].get() == 1: self.possible_selections.append((difficulty, category))
	
	def _getRandomCategory(self):
		return random.choice(self.possible_selections)
	
	def _getRandomQuestion(self, category):
		pass

	def getQuestion():
		yield 