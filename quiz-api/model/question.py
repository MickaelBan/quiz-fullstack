



class Question():
	def __init__(self, title: str, position: str, text: str, image:str, possibleAnswers):
		self.title = title
		self.position = position
		self.text = text
		self.image = image
		self.possibleAnswers = possibleAnswers
		# if possibleAnswers:
		# 	[self.setAnswer(possibleAnswers[i,0],possibleAnswers[i,1]) for i in range(len(possibleAnswers))]
  
	def setAnswer(self,text,isCorect):
		self.answers.append([text,isCorect]) 