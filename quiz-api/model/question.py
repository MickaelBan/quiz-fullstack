from flask import jsonify
from sqlite3 import Cursor

class Question():
    def __init__(self, title: str, position: str, text: str, image: str, possibleAnswers):
        if title is not None and "'" in title:
            title = title.replace("'","''")
        if text is not None and "'" in text:
            text = text.replace("'","''")
        if image is not None and "'" in image:
            image = image.replace("'","''")
        
        self.title = title
        self.position = position
        self.text = text
        self.image = image
        self.possibleAnswers = possibleAnswers
    
    def parseQuestionToJson(self) -> str:
        if self.title is not None and "''" in self.title:
            self.title = self.title.replace("''","'")
        if self.text is not None and "'" in self.text:
            self.text = self.text.replace("''","'")
        if self.image is not None and "'" in self.image:
            self.image = self.image.replace("''","'")
        
        json = {"title": self.title, "position": self.position, "text": self.text,
                "image": self.image, "possibleAnswers": self.possibleAnswers}
        
        return jsonify(json)

    @staticmethod
    def parseRequestToQuestion(request):
        js = request.get_json()
        return Question(title=js['title'],
                        position=js['position'],
                        text=js['text'],
                        image=js['image'],
                        possibleAnswers=js['possibleAnswers'])
    
    @staticmethod
    def parseDbToQuestion(cursor:Cursor,questionId):
        cursor.execute("SELECT * FROM questions INNER JOIN possibleAnswers ON questions.id = idQuestion WHERE questions.id = " + str(questionId))
        fetchall = cursor.fetchall()
        position = fetchall[0][1]
        
        if fetchall[0][2] is not None and "''" in fetchall[0][2]:
            fetchall[0][2] = str(fetchall[0][2]).replace("''","'")
        else :
            title = fetchall[0][2]
        if fetchall[0][3] is not None and "''" in fetchall[0][3]:
            text = str(fetchall[0][3]).replace("''","'")
        else :
            text = fetchall[0][3]
        
        image = fetchall[0][4]
        possibleAnswers = []
        for i in range(len(fetchall)):            
            possibleAnswers.append({"text":fetchall[i][6],"isCorrect":fetchall[i][7] in ['True']})
        possibleAnswers = possibleAnswers
        
        return Question(title,position,text,image,possibleAnswers)
        