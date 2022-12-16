



class Question():
	def __init__(self, title: str, position: str, text: str, image:str, possibleAnswers):
		self.title = title.replace("'","''")
		self.position = position
		self.text = text.replace("'","''")
		self.image = image.replace("'","''")
		self.possibleAnswers = possibleAnswers