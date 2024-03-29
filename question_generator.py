import random

class QuestionGenerator():
	def __init__(self, categories, selections) -> None:
		self.categories = categories
		self.selections = selections

		self.possible_selections = []

		for category in self.categories:
			for difficulty in ["Basic", "Advanced"]:
				if selections[difficulty+category].get() == 1: self.possible_selections.append((difficulty, category))
	
	def _getRandomDifficultyAndCategory(self):
		return random.choice(self.possible_selections) if self.possible_selections else ("Basic", "Addition")
	
	def _getRandomNumbers(self, difficult):
		if difficult:
			num1 = random.randint(1, 99)
			num2 = random.randint(1, 99)
		else:
			num1 = random.randint(0, 10)
			num2 = random.randint(0, 10)
		return num1, num2
	
	def _getAdditionQuestion(self, difficult):
		num1, num2 = self._getRandomNumbers(difficult)
		return (f"{num1} + {num2}", num1+num2)
	
	def _getSubtractionQuestion(self, difficult):
		num1, num2 = self._getRandomNumbers(difficult)
		greater = num1 if num1 > num2 else num2
		lesser = num1 if num1 != greater else num2
		return (f"{greater} - {lesser}", greater-lesser)
	
	def _getMultiplicationQuestion(self, difficult):
		num1, num2 = self._getRandomNumbers(difficult)
		return (f"{num1} x {num2}", num1*num2)
	
	def _getDivisionQuestion(self, difficult):
		if difficult:
			divisor = random.randint(1, 99)
			quotient = random.randint(0, 99)
			dividend = divisor*quotient
		else:
			divisor = random.randint(1, 10)
			quotient = random.randint(0, 10)
			dividend = divisor*quotient
		return (f"{dividend} / {divisor}", quotient)
	
	def _getExponentiationQuestion(self, difficult):
		if difficult:
			base = random.randint(1, 9)
			exponent = random.randint(0, 5)
		else:
			base = random.randint(1, 20)
			exponent = 2
		return (f"{base}^{exponent}", base**exponent)
	
	def _getRootQuestion(self, difficult):
		if difficult:
			base = random.randint(1, 9)
			exponent = random.randint(0, 5)
		else:
			base = random.randint(1, 20)
			exponent = 2
		return (f"{exponent}√{base**exponent}", base)
	
	def _getRandomQuestion(self):
		difficulty, category = self._getRandomDifficultyAndCategory()
		difficult = difficulty != "Basic"

		functionMap = {
			"Addition": self._getAdditionQuestion,
			"Subtraction": self._getSubtractionQuestion,
			"Multiplication": self._getMultiplicationQuestion,
			"Division": self._getDivisionQuestion,
			"Exponentiation": self._getExponentiationQuestion,
			"Root Extraction": self._getRootQuestion,
		}

		return functionMap[category](difficult)

	def getQuestionAndAnswer(self):
		return self._getRandomQuestion()