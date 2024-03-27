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
	
	def _getRandomQuestion(self):
		difficulty, category = self._getRandomDifficultyAndCategory()
		difficult = 0 if difficulty == "Basic" else 1

		if difficult:
			num1 = random.randint(1, 99)
			num2 = random.randint(1, 99)
		else:
			num1 = random.randint(0, 10)
			num2 = random.randint(0, 10)

		match category:
			case "Addition":
				return (f"{num1} + {num2}", num1+num2)
			case "Subtraction":
				greater = num1 if num1 > num2 else num2
				lesser = num1 if num1 != greater else num2
				return (f"{greater} - {lesser}", greater-lesser)
			case "Multiplication":
				return (f"{num1} x {num2}", num1*num2)
			case "Division":
				if difficult:
					divisor = random.randint(1, 99)
					quotient = random.randint(0, 99)
					dividend = divisor*quotient
				else:
					divisor = random.randint(1, 10)
					quotient = random.randint(0, 10)
					dividend = divisor*quotient
				return (f"{dividend} / {divisor}", quotient)
			case "Exponentiation":
				if difficult:
					base = random.randint(1, 9)
					exponent = random.randint(0, 5)
				else:
					base = random.randint(1, 20)
					exponent = 2
				return (f"{base}^{exponent}", base**exponent)
			case "Root Extraction":
				if difficult:
					base = random.randint(1, 9)
					exponent = random.randint(0, 5)
				else:
					base = random.randint(1, 20)
					exponent = 2
				return (f"{exponent} root {base**exponent}", base)

	def getQuestionAndAnswer(self):
		return self._getRandomQuestion()